#!/bin/bash

# 用法: bash scripts/create_schema.sh <suffix> [project1] [project2] ...
# 示例:
#   bash scripts/create_schema.sh "_decomposed_tests" maven
#   bash scripts/create_schema.sh "_decomposed_tests"

if [ $# -lt 1 ]; then
  echo "Usage: $0 <suffix> [project_name1] [project_name2] ..."
  echo ""
  echo "Arguments:"
  echo "  suffix      - 后缀 (如 _decomposed_tests)"
  echo "  project     - 项目名称 (可选，默认全部)"
  echo ""
  echo "Examples:"
  echo "  $0 '_decomposed_tests' maven"
  echo "  $0 '_decomposed_tests'"
  exit 1
fi

suffix="$1"
shift

if [ $# -eq 0 ]; then
  # 默认项目列表
  PROJECTS=('commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR')
else
  PROJECTS=("$@")
fi

for project in "${PROJECTS[@]}"
do
    echo "Creating schema for $project"
    python3 src/static_analysis/create_schema.py --project_name=$project --suffix=$suffix
done
