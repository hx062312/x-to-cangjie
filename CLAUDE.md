# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

AlphaTrans 是一个神经符号混合的代码翻译框架，用于将 Java 项目翻译为 Python。项目被 FSE 2025 会议接收。

核心工作流程：
1. **项目缩减** - 移除第三方依赖
2. **程序转换** - 转换重载方法和构造函数
3. **测试分解** - 将测试分解为独立片段
4. **CodeQL 分析** - 创建数据库并进行静态分析
5. **组合翻译** - 按反向调用图顺序翻译代码片段
6. **多级验证** - 语法正确性、GraalVM 正确性、测试执行正确性

## 环境设置

项目通过 Docker 运行：

```bash
docker build --no-cache -t alphatrans .
docker run -it alphatrans bash
```

Mac M 系列芯片需添加 `--platform=linux/amd64` 参数。

模型配置编辑 `configs/model_configs.yaml`。

## 常用命令

### 翻译已有预处理结果的项目

```bash
# 获取依赖并生成测试调用图
bash scripts/get_dependencies.sh _decomposed_tests
bash scripts/generate_test_invocation_map.sh _decomposed_tests
bash scripts/extract_coverage.sh commons-fileupload _decomposed_tests

# 执行翻译
bash scripts/translate_fragment.sh commons-fileupload 0.0 gpt-4o-2024-11-20

# 查看结果
bash scripts/print_results.sh commons-fileupload 0.0 gpt-4o-2024-11-20 data/schemas_decomposed_tests/translations

# 重组为独立 Python 项目
bash scripts/recompose.sh commons-fileupload 0.0 gpt-4o-2024-11-20
```

### 新项目翻译流程

完整流程分为两个阶段：

#### 阶段一：项目预处理（必选）

从原始 Java 项目开始，需要依次完成：

```bash
# 1. 项目缩减 - 移除第三方依赖
bash scripts/add_plugin.sh <project_name>
bash scripts/merge_jar.sh <project_name>
bash scripts/generate_cg.sh <project_name>
python3 src/preprocessing/reduce_third_party_libs.py <project_name>

# 2. 程序转换 - 转换重载方法和构造函数
# 需先创建 CodeQL 数据库
bash scripts/method_transformation.sh <project_name>
bash scripts/constructor_transformation.sh <project_name>

# 3. 测试分解 - 将测试分解为独立片段
bash scripts/extract_coverage.sh <project_name> ''
bash scripts/decompose_test.sh
```

结果保存在 `java_projects/cleaned_final_projects_decomposed_tests/`

> 注意：测试分解后可能需要手动调整，如移除 `@Test(expected = ...)` 注解。只要 Maven 能编译即可。

#### 阶段二：CodeQL 分析与翻译

预处理完成后，执行以下步骤：

```bash
# 1. CodeQL 数据库创建
bash scripts/create_database.sh _decomposed_tests

# 2. 执行 CodeQL 查询
cd vscode-codeql-starter/codeql-custom-queries-java && bash run.sh

# 3. 程序分解
bash scripts/create_schema.sh _decomposed_tests
bash scripts/extract_call_graph.sh _decomposed_tests

# 4. 骨架构建
bash scripts/create_skeleton.sh _decomposed_tests

# 5. 组合翻译
bash scripts/translate_fragment.sh <project_name> <temperature> <model>
```

### 分析命令

```bash
# 测试分解效果分析
bash scripts/analyze_test_decomposition.sh <model_name> <translation_dir>

# ATP+ 和 TPR+ 计算
python3 src/postprocessing/atp_tpr_plus.py --project_name=<project_name>
```

## 项目结构

- `src/` - Python 源代码（预处理、后处理、翻译逻辑）
- `scripts/` - 各种自动化脚本
- `queries/` - CodeQL 查询
- `configs/` - 模型配置
- `data/` - 类型映射、schemas、查询输出、翻译结果
- `java_projects/` - Java 项目快照目录（预处理流程的中间/最终结果）：
  - `original_projects/` - GitHub 克隆的原始项目
  - `automated_reduced_projects/` - 项目缩减后
  - `preprocessed_0/` - 方法转换后
  - `cleaned_final_projects/` - 构造函数转换后
  - `cleaned_final_projects_decomposed_tests/` - 测试分解后（推荐作为翻译起点）
- `databases/` - CodeQL 数据库

## 依赖项

- Docker
- CodeQL CLI
- Java (用于项目处理)
- Python 3
- 支持的 LLM：OpenAI GPT-4o、DeepSeek Coder 等（通过 ollama 或 vLLM 提供）

## 注意事项

- 项目已提供预处理结果：`java_projects/cleaned_final_projects_decomposed_tests/`，从此开始可节省数小时
- 预处理流程耗时较长，建议直接使用提供的快照
- 翻译结果保存在 JSON 文件中，包含各类验证结果
- `extract_coverage.sh` 执行时间较长
- 模型结果可能因 LLM 概率特性略有差异
