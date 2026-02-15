# AlphaTrans 类翻译流程文档

本文档详细描述了 AlphaTrans 框架将 Java 类翻译为 Python 的完整流程。以 `LimitedInputStream` 类为例进行说明。

## 1. 概述

AlphaTrans 采用神经符号混合的翻译策略，结合了 LLM 的生成能力和多级验证管线。翻译流程的核心思想是：

1. **反向拓扑排序** - 按照调用依赖关系反向翻译，确保依赖类先被翻译
2. **骨架填充** - 先通过静态分析生成 Python 骨架，再由 LLM 填充实现
3. **多级验证** - 依次进行语法、执行、GraalVM、测试验证
4. **自适应重试** - 根据验证失败类型动态调整重试预算

## 2. Java 源文件结构

### 2.1 LimitedInputStream 源文件

路径: `java_projects/cleaned_final_projects_decomposed_tests/commons-fileupload/src/main/java/org/apache/commons/fileupload/util/LimitedInputStream.java`

```java
public abstract class LimitedInputStream extends FilterInputStream implements Closeable {
    private final long sizeMax;      // 最大字节数限制
    private long count;              // 当前已读取字节数
    private boolean closed;          // 流是否已关闭

    public LimitedInputStream(InputStream inputStream, long pSizeMax) { ... }
    protected abstract void raiseError(long pSizeMax, long pCount) throws IOException;
    private void checkLimit() throws IOException { ... }
    public int read0() throws IOException { ... }
    public int read1(byte[] b, int off, int len) throws IOException { ... }
    public boolean isClosed() throws IOException { ... }
    public void close() throws IOException { ... }
}
```

### 2.2 关键特征

- **继承关系**: `extends FilterInputStream implements Closeable`
- **抽象方法**: `raiseError` 需要子类实现
- **内部调用**: `read0/read1` 调用 `checkLimit`，`checkLimit` 调用 `raiseError`

## 3. CodeQL 分析生成 Schema

### 3.1 Schema 生成脚本

```bash
bash scripts/create_schema.sh _decomposed_tests
```

### 3.2 Schema JSON 结构

Schema 文件位置: `data/schemas_decomposed_tests/translations/gpt-4o-2024-11-20/body/0.0/commons-fileupload/commons-fileupload.src.main.org.apache.commons.fileupload.util.LimitedInputStream_python_partial.json`

```json
{
  "path": "java_projects/.../LimitedInputStream.java",
  "imports": {
    "20-20:import IOException": { "start": 20, "end": 20, "body": ["import java.io.IOException;\n"] },
    "21-21:import InputStream": { ... },
    "19-19:import FilterInputStream": { ... }
  },
  "classes": {
    "LimitedInputStream": {
      "start": 27,
      "end": 27,
      "is_abstract": true,
      "is_interface": false,
      "extends": [],
      "implements": [],
      "nests": [],
      "nested_inside": [],
      "python_class_declaration": "class LimitedInputStream(ABC):\n\n",
      "methods": {
        "138-141:close": {
          "start": 138,
          "end": 141,
          "body": ["    public void close() throws IOException {\n", "        closed = true;\n", "        super.close();\n", "    }\n"],
          "is_constructor": false,
          "annotations": ["Override"],
          "modifiers": ["public"],
          "return_types": [["void", "void"]],
          "signature": "close()",
          "parameters": [],
          "calls": [["library", "java.base/java/io/FilterInputStream", "close()"]],
          "is_overload": false,
          "partial_translation": [
            "    def close(self) -> None:\n",
            "        pass\n\n"
          ],
          "translation": [],
          "translation_status": "pending",
          "syntactic_validation": "pending",
          "field_exercise": "pending",
          "graal_validation": "pending",
          "test_execution": "pending",
          ...
        },
        "45-48:LimitedInputStream": {
          "is_constructor": true,
          "signature": "LimitedInputStream(InputStream, long)",
          "partial_translation": [
            "    def __init__(self, inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader], pSizeMax: int) -> None:\n",
            "        pass\n\n"
          ],
          ...
        }
      },
      "fields": {
        "36-36:closed": {
          "body": ["    private boolean closed;\n"],
          "modifiers": ["private"],
          "types": [["boolean", "boolean"]],
          "partial_translation": ["    __closed: bool = False", ""],
          "translation_status": "pending",
          ...
        },
        "30-30:sizeMax": { ... },
        "33-33:count": { ... }
      }
    }
  },
  "python_imports": [
    "from __future__ import annotations",
    "from abc import ABC",
    "from io import StringIO",
    "import io",
    "from io import BytesIO",
    "import typing\nfrom typing import *",
    "import os",
    "from src.main.org.apache.commons.fileupload.util.Closeable import *"
  ]
}
```

### 3.3 关键 Schema 字段说明

| 字段 | 说明 |
|------|------|
| `python_class_declaration` | Python 类声明骨架 |
| `partial_translation` | 方法/字段的 Python 签名骨架（`pass` 占位） |
| `calls` | 方法调用的依赖关系 `[schema, class, method]` |
| `translation` | LLM 翻译的实际实现代码 |
| `translation_status` | 翻译状态：`pending` / `attempted` / `out_of_context` |
| `syntactic_validation` | 语法验证结果：`pending` / `parseable` / `non-parseable` |
| `field_exercise` | 字段执行验证：`pending` / `success` / `failed` |
| `graal_validation` | GraalVM 验证结果 |
| `test_execution` | 测试执行结果 |

## 4. 骨架构建

### 4.1 脚本

```bash
bash scripts/create_skeleton.sh _decomposed_tests
```

### 4.2 骨架生成逻辑

骨架文件位置: `data/skeletons/commons-fileupload/src/main/org/apache/commons/fileupload/util/LimitedInputStream.py`

```python
from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.util.Closeable import *
import os
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO
from abc import ABC
# Imports End

class LimitedInputStream(ABC):
    # Class Fields Begin
    __sizeMax: int = None
    __count: int = None
    __closed: bool = None
    # Class Fields End

    # Class Methods Begin
    def close(self) -> None:
        pass

    def isClosed(self) -> bool:
        pass

    def read1(self, b: typing.List[int], off: int, len_: int) -> int:
        pass

    def read0(self) -> int:
        pass

    def __init__(self, inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader], pSizeMax: int) -> None:
        pass

    def __checkLimit(self) -> None:
        pass

    def _raiseError(self, pSizeMax: int, pCount: int) -> None:
        pass
    # Class Methods End
```

### 4.3 类型映射规则

在骨架生成过程中，Java 类型被映射为 Python 类型：

| Java 类型 | Python 类型 |
|-----------|-------------|
| `boolean` | `bool` |
| `int` / `long` | `int` |
| `String` | `str` |
| `InputStream` | `typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]` |
| `byte[]` | `typing.List[int]` |
| `FilterInputStream` (基类) | `ABC` (抽象基类) |

## 5. 反向调用图遍历

### 5.1 脚本

翻译入口脚本: `scripts/translate_fragment.sh`

```bash
bash scripts/translate_fragment.sh commons-fileupload 0.0 gpt-4o-2024-11-20
```

### 5.2 核心逻辑

文件: `src/translation/get_reverse_traversal.py`

```python
def get_reverse_traversal(args):
    """
    基于调用依赖生成反向拓扑排序的翻译顺序
    1. 字段 (field)
    2. 静态初始化器 (static_initializer)
    3. 主类方法 (main class methods)
    4. 测试类方法 (test class methods)
    """
```

### 5.3 LimitedInputStream 的翻译顺序

对于 `LimitedInputStream`，翻译顺序如下：

1. **字段** (按依赖排序):
   - `sizeMax` (无依赖)
   - `count` (无依赖)
   - `closed` (无依赖)

2. **方法** (按反向调用图):
   - `raiseError` (抽象方法，无内部调用) → 先翻译
   - `checkLimit` (调用 `raiseError`) → 后翻译
   - `read0` / `read1` (调用 `checkLimit`) → 后翻译
   - `isClosed` / `close` (无内部调用) → 可并行

3. **等待队列处理**:
   - 如果方法 A 调用方法 B，但 B 尚未翻译，则 A 进入等待队列
   - 处理循环检测并展开循环依赖

## 6. LLM 翻译

### 6.1 入口函数

文件: `src/translation/compositional_translation_validation.py`

```python
def translate(fragment, args, processed_fragments, budget={}, feedback=None, recursion_depth=2):
    # 1. 计算自适应预算
    # 2. 循环处理各验证阶段
    # 3. 调用 LLM 生成翻译
```

### 6.2 Prompt 生成

文件: `src/translation/prompt_generator.py`

```python
class PromptGenerator:
    def build_base_prompt(self):
        # 1. 添加 persona
        # 2. 添加 In-Context Learning 示例
        # 3. 添加指令
        # 4. 添加源代码
        # 5. (如需要) 添加错误翻译和反馈
        # 6. 添加部分翻译 (partial_translation)
        # 7. 添加目标翻译格式
```

### 6.3 LimitedInputStream 示例 Prompt

```
You are a helpful assistant.

### In-Context Learning Example
Java code:
```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
}
```

Partial Python translation:
```python
class Calculator:
    def add(self, a: int, b: int) -> int:
        pass
```

Python method translation:
```python
    def add(self, a: int, b: int) -> int:
        return a + b
```

### Instruction:
Translate the following Java method to Python 3.10 like the example above.
You only need to translate the "close" method.
All necessary dependencies are available in partial Python translation.

### Java code:
```java
class LimitedInputStream {
    private boolean closed;

    public void close() throws IOException {
        closed = true;
        super.close();
    }
}
```

### Partial Python translation:
```python
from __future__ import annotations
from abc import ABC
...

class LimitedInputStream(ABC):
    __closed: bool = False

    def close(self) -> None:
        pass
```

### Response:
Python method translation:
```python
    def close(self) -> None:
        self.__closed = True
        super().close()
```

### 6.4 API 调用与解析

```python
def prompt_model(model_info, client, prompt, total_input_tokens, args):
    completion = client.chat.completions.create(
        model=model_info[args.model_name]['model_id'],
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_new_tokens,
        temperature=args.temperature,
        ...
    )
    generation = completion.choices[0].message.content
    return generation
```

## 7. 多级验证管线

### 7.1 验证流程图

```
┌─────────────────┐
│  LLM 生成代码   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  语法验证       │ ── 失败 ──▶ 重试 (syntactic budget)
│ (syntactic)     │ ── 通过 ──▶
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  字段执行验证   │ ── 失败 ──▶ 重试 (field_exercise budget)
│ (field_exercise)│ ── 通过 ──▶
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  GraalVM 验证  │ ── 失败 ──▶ 重试 (graal budget)
│ (graal)        │ ── 通过 ──▶
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  测试执行验证  │ ── 失败 ──▶ 定位可疑方法并重试
│ (test_execution)│
└─────────────────┘
```

### 7.2 语法验证

文件: `src/translation/syntactic_validation.py`

```python
def syntactic_validation(generation, fragment, args, signature):
    # 1. 从 LLM 输出中提取代码块
    # 2. 使用 AST 解析验证语法正确性
    # 3. 应用异常映射和常量映射
    # 4. 返回验证结果和修正后的代码
```

验证逻辑:
- 使用正则提取 ```python ... ``` 代码块
- 使用 `ast.parse()` 验证 Python 语法
- 提取目标方法签名并验证存在性

### 7.3 字段执行验证

文件: `src/translation/field_exercise_validation.py`

```python
def field_exercise_validation(fragment, args):
    # 1. 重组 Python 项目
    # 2. 执行类文件（验证字段初始化）
    # 3. 返回执行结果
```

### 7.4 GraalVM 验证

文件: `src/translation/graal_validation.py`

```python
def graal_validation(generation, fragment, args):
    # 1. 注入翻译到重组项目
    # 2. 派生组合测试
    # 3. 执行 GraalVM 测试
    # 4. 返回验证结果
```

### 7.5 测试执行验证

文件: `src/translation/test_validation.py`

```python
def test_validation(args, eligible_tests):
    # 1. 重组完整 Python 项目
    # 2. 执行相关测试
    # 3. 计算覆盖率
    # 4. 返回测试结果
```

## 8. 自适应重试机制 (Budget 系统)

### 8.1 预算分配

文件: `src/translation/compositional_translation_validation.py`

```python
def get_adaptive_budget(fragment, args, feedback=False):
    if fragment['fragment_type'] in ['field', 'static_initializer']:
        return 2 if not feedback else 1
    elif fragment['fragment_type'] == 'method' and fragment['is_test_method']:
        return 2 if not feedback else 1

    # 主类方法：根据测试覆盖率动态计算
    total_executed_tests = ...
    total_covered = ...
    max_budget = max(math.ceil(5 * (total_covered / total_executed_tests)), 2)
    return min(5, max_budget) if not feedback else 1
```

### 8.2 预算结构

```python
budget = {
    'syntactic': 3,       # 语法验证重试次数
    'field_exercise': 3,  # 字段执行验证重试次数
    'graal': 3,           # GraalVM 验证重试次数
    'test_execution': 3   # 测试执行重试次数
}
```

### 8.3 重试逻辑

```python
while budget[current_budget] > 0:
    # 1. 执行当前阶段验证
    status, feedback = validation_func(...)

    # 2. 验证失败且还有预算时，重试
    if not status:
        budget[current_budget] -= 1
        continue

    # 3. 验证通过，进入下一阶段
    break
```

## 9. 关键文件路径汇总

| 阶段 | 文件路径 |
|------|----------|
| Java 源文件 | `java_projects/cleaned_final_projects_decomposed_tests/commons-fileupload/src/main/java/org/apache/commons/fileupload/util/LimitedInputStream.java` |
| Schema | `data/schemas_decomposed_tests/translations/gpt-4o-2024-11-20/body/0.0/commons-fileupload/commons-fileupload.src.main.org.apache.commons.fileupload.util.LimitedInputStream_python_partial.json` |
| 骨架 | `data/skeletons/commons-fileupload/src/main/org/apache/commons/fileupload/util/LimitedInputStream.py` |
| 翻译核心 | `src/translation/compositional_translation_validation.py` |
| Prompt 生成 | `src/translation/prompt_generator.py` |
| 反向遍历 | `src/translation/get_reverse_traversal.py` |
| 语法验证 | `src/translation/syntactic_validation.py` |
| 字段验证 | `src/translation/field_exercise_validation.py` |
| GraalVM 验证 | `src/translation/graal_validation.py` |
| 测试验证 | `src/translation/test_validation.py` |
| 重组项目 | `data/recomposed_projects/gpt-4o-2024-11-20/body/0.0/commons-fileupload/` |

## 10. 运行命令

### 10.1 完整翻译流程

```bash
# 1. 获取依赖
bash scripts/get_dependencies.sh _decomposed_tests

# 2. 生成测试调用图
bash scripts/generate_test_invocation_map.sh _decomposed_tests

# 3. 提取覆盖率
bash scripts/extract_coverage.sh commons-fileupload _decomposed_tests

# 4. 执行翻译
bash scripts/translate_fragment.sh commons-fileupload 0.0 gpt-4o-2024-11-20

# 5. 查看结果
bash scripts/print_results.sh commons-fileupload 0.0 gpt-4o-2024-11-20 data/schemas_decomposed_tests/translations

# 6. 重组为独立 Python 项目
bash scripts/recompose.sh commons-fileupload 0.0 gpt-4o-2024-11-20
```

### 10.2 调试模式

```bash
python3 src/translation/compositional_translation_validation.py \
    --model_name=gpt-4o-2024-11-20 \
    --project_name=commons-fileupload \
    --from_lang=Java \
    --to_lang=Python \
    --include_call_graph \
    --debug \
    --suffix=_decomposed_tests \
    --temperature=0.0 \
    --validate_by_graal \
    --recursion_depth=2 \
    --include_implementation
```

## 11. 状态追踪

Schema 中的每个方法/字段都包含完整的状态追踪：

```json
{
  "translation_status": "attempted",      // pending | attempted | out_of_context
  "syntactic_validation": "parseable",     // pending | parseable | non-parseable
  "field_exercise": "success",            // pending | success | failed
  "graal_validation": "pending",          // pending | success | failed | not-exercised
  "test_execution": "pending",            // pending | exercised-success | exercised-failed | not-exercised
  "elapsed_time": 1.23,
  "generation_timestamp": "2026-02-15T16:01:47.929824",
  "original_budget": { ... },
  "final_budget": { ... }
}
```
