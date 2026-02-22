#!/bin/bash

# 用法: bash scripts/init_codeql_db.sh <project_name> [source_dir] [output_suffix]
# 示例:
#   bash scripts/init_codeql_db.sh maven automated_reduced_projects ""
#   bash scripts/init_codeql_db.sh maven preprocessed_0 ""
#   bash scripts/init_codeql_db.sh maven cleaned_final_projects "_transformed"
#   bash scripts/init_codeql_db.sh maven cleaned_final_projects_decomposed_tests "_decomposed_tests"

if [ $# -lt 1 ]; then
  echo "Usage: $0 <project_name> [source_dir] [output_suffix]"
  echo ""
  echo "Arguments:"
  echo "  project_name   - 项目名称 (如 maven)"
  echo "  source_dir     - 源目录 (默认: automated_reduced_projects)"
  echo "  output_suffix  - 输出后缀 (默认: 空)"
  echo ""
  echo "Examples:"
  echo "  $0 maven automated_reduced_projects ''"
  echo "  $0 maven cleaned_final_projects_decomposed_tests '_decomposed_tests'"
  exit 1
fi

PROJECT_NAME="$1"
SOURCE_DIR="${2:-automated_reduced_projects}"
OUTPUT_SUFFIX="${3:-}"

# 获取脚本所在目录的绝对路径，然后定位到项目根目录
SCRIPT_DIR=$(dirname "$(realpath "$0")")
PROJECT_ROOT=$(cd "$SCRIPT_DIR/.." && pwd)

PROJECT_DIR="${PROJECT_ROOT}/java_projects/${SOURCE_DIR}/${PROJECT_NAME}"
OUTPUT_DIR="${PROJECT_ROOT}/databases/${PROJECT_NAME}${OUTPUT_SUFFIX}"

if [ ! -d "$PROJECT_DIR" ]; then
  echo "Error: Project directory '$PROJECT_DIR' does not exist."
  exit 1
fi

mkdir -p "$(dirname "$OUTPUT_DIR")"

echo "=========================================="
echo "Creating CodeQL database for: $PROJECT_NAME"
echo "Source:      $PROJECT_DIR"
echo "Output:      $OUTPUT_DIR"
echo "=========================================="

cd "$PROJECT_DIR" || exit 1

# 创建 CodeQL 数据库
codeql database create "$OUTPUT_DIR" --language=java --overwrite

if [ $? -eq 0 ]; then
  echo "Success! Database created at: $OUTPUT_DIR"
else
  echo "Error: Failed to create database"
  exit 1
fi
