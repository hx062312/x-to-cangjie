# 翻译示例：DiskFileItemFactory.setDefaultCharset()

本文档通过一个具体的例子，展示 AlphaTrans 框架如何将 Java 代码翻译为 Python。

---

## 示例方法：`DiskFileItemFactory.setDefaultCharset()`

### 1. 原始 Java 代码

**文件**: `java_projects/cleaned_final_projects_decomposed_tests/commons-fileupload/src/main/java/org/apache/commons/fileupload/disk/DiskFileItemFactory.java`

```java
// 第 79 行
private String defaultCharset = DiskFileItem.DEFAULT_CHARSET;

// setter 方法
public void setDefaultCharset(String pCharset) {
    defaultCharset = pCharset;
}

// getter 方法
public String getDefaultCharset() {
    return defaultCharset;
}
```

### 2. 预处理后的代码

经过预处理阶段（项目缩减、程序转换、测试分解），Java 代码保持不变，但会生成 schema 文件描述类结构。

### 3. Schema 结构 (JSON)

**文件**: `data/schemas_decomposed_tests/translations/gpt-4o-2024-11-20/body/0.0/commons-fileupload/commons-fileupload.src.main.org.apache.commons.fileupload.disk.DiskFileItemFactory_python_partial.json`

```json
{
    "classes": {
        "DiskFileItemFactory": {
            "fields": {
                "79-79:defaultCharset": {
                    "start": 79,
                    "end": 79,
                    "body": ["private String defaultCharset = DiskFileItem.DEFAULT_CHARSET;"],
                    "modifiers": ["private"],
                    "return_types": [["String", "String"]]
                }
            },
            "methods": {
                "80-82:setDefaultCharset": {
                    "start": 80,
                    "end": 82,
                    "body": [
                        "    public void setDefaultCharset(String pCharset) {",
                        "        defaultCharset = pCharset;",
                        "    }"
                    ],
                    "modifiers": ["public"],
                    "return_types": [["void", "void"]],
                    "parameters": ["pCharset"],
                    "calls": []
                }
            }
        }
    }
}
```

### 4. LLM 翻译结果

系统调用 GPT-4o 模型进行翻译，模型生成的 Python 代码：

```python
# 字段翻译
"translation": [
    "    __defaultCharset: str = DiskFileItem.DEFAULT_CHARSET"
]

# 方法翻译
"translation": [
    "    def setDefaultCharset(self, pCharset: str) -> None:",
    "        self.__defaultCharset = pCharset"
]
```

### 5. 验证状态

每个翻译都有完整的验证追踪：

```json
{
    "translation_status": "attempted",
    "syntactic_validation": "parseable",     # Python 语法正确
    "field_exercise": "success",            # 字段访问正确
    "graal_validation": "pending",         # 待 GraalVM 验证
    "test_execution": "pending",           # 待测试验证
    "elapsed_time": 55.41,
    "generation_timestamp": "2026-02-15T16:16:06.244230"
}
```

### 6. 重组后的 Python 文件

**文件**: `data/recomposed_projects/gpt-4o-2024-11-20/body/0.0/commons-fileupload/src/main/org/apache/commons/fileupload/disk/DiskFileItemFactory.py`

```python
from __future__ import annotations
import pathlib

class DiskFileItemFactory:

    DEFAULT_SIZE_THRESHOLD: int = None
    __defaultCharset: str = None
    __sizeThreshold: int = None
    __repository: pathlib.Path = None

    def setDefaultCharset(self, pCharset: str) -> None:
        pass  # LLM could not translate this method
```

> 注意：重组时只有骨架（方法签名），实际翻译内容在单独的 JSON 文件中。

---

## 翻译流程概览

```
┌─────────────────────────────────────────────────────────────┐
│ 1. 预处理阶段                                               │
│    - 项目缩减：移除第三方依赖                                │
│    - 程序转换：处理重载方法                                  │
│    - 测试分解：将测试拆分为独立片段                          │
│    - CodeQL 分析：提取调用图、创建 schema                   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. 翻译阶段                                                 │
│    a) 按反向调用图顺序翻译依赖类                             │
│    b) PromptGenerator 生成翻译提示                         │
│    c) 调用 LLM (GPT-4o/DeepSeek Coder)                    │
│    d) 多级验证：                                            │
│       - 语法验证 (syntactic_validation)                    │
│       - 字段验证 (field_exercise)                          │
│       - GraalVM 验证 (graal_validation)                    │
│       - 测试执行 (test_execution)                          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. 重组阶段                                                 │
│    - recompose.py 将翻译片段组合成完整的 Python 项目          │
│    - 生成 __init__.py 文件                                   │
│    - 创建可运行的 Python 项目结构                           │
└─────────────────────────────────────────────────────────────┘
```

---

## 关键文件路径

| 阶段 | 路径 |
|------|------|
| 原始 Java | `java_projects/cleaned_final_projects_decomposed_tests/commons-fileupload/src/main/java/org/apache/commons/fileupload/disk/DiskFileItemFactory.java` |
| Schema/翻译结果 | `data/schemas_decomposed_tests/translations/gpt-4o-2024-11-20/body/0.0/commons-fileupload/commons-fileupload.src.main.org.apache.commons.fileupload.disk.DiskFileItemFactory_python_partial.json` |
| 重组后 Python | `data/recomposed_projects/gpt-4o-2024-11-20/body/0.0/commons-fileupload/src/main/org/apache/commons/fileupload/disk/DiskFileItemFactory.py` |
| 翻译脚本 | `src/translation/compositional_translation_validation.py` |

---

## 相关文档

- [CLAUDE.md](../CLAUDE.md) - 项目概述和使用说明
- [README.md](../README.md) - 完整项目文档
