#!/bin/bash

# 用法: bash queries/run.sh <project_name> [suffix]
# 示例:
#   bash queries/run.sh maven ""           # 数据库: maven, 输出: query_outputs
#   bash queries/run.sh maven "_decomposed_tests"  # 数据库: maven_decomposed_tests, 输出: query_outputs_decomposed_tests

if [ $# -lt 1 ]; then
  echo "Usage: $0 <project_name> [suffix]"
  echo ""
  echo "Arguments:"
  echo "  project_name - 项目名称 (如 maven)"
  echo "  suffix      - 数据库后缀 (默认: '')"
  echo ""
  echo "Examples:"
  echo "  $0 maven"
  echo "  $0 maven '_decomposed_tests'"
  exit 1
fi

PROJECT_NAME="$1"
SUFFIX="${2:-}"
DATABASE_NAME="${PROJECT_NAME}${SUFFIX}"
# 输出路径不带 data/ 前缀，因为 execute_queries.py 会自动添加到 data/ 下
OUTPUT_PATH="query_outputs${SUFFIX}"

SCRIPT_DIR=$(dirname "$(realpath "$0")")
# 需要在 vscode-codeql-starter/codeql-custom-queries-java/ 目录下运行
# 因为那里有 qlpack.yml 配置 CodeQL Java 语言库
CODEQL_DIR="${SCRIPT_DIR}/../vscode-codeql-starter/codeql-custom-queries-java"
cd "$CODEQL_DIR" || exit 1

echo "=========================================="
echo "Running CodeQL queries for: $PROJECT_NAME"
echo "Database:      $DATABASE_NAME"
echo "Output:        $OUTPUT_PATH"
echo "=========================================="

bash execute_codeql_queries.sh "$PROJECT_NAME" "$DATABASE_NAME" "$OUTPUT_PATH"

echo "Done! Results saved to: $OUTPUT_PATH"
