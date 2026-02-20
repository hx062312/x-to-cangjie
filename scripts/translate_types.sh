#!/bin/bash

# 用法: bash scripts/translate_types.sh <type> <model_name> [project1] [project2] ...

if [ $# -lt 2 ]; then
  echo "Usage: $0 <type> <model_name> [project_name1] [project_name2] ..."
  echo ""
  echo "Arguments:"
  echo "  type       - 类型 (如 ShoppingCart, CartItem)"
  echo "  model_name - 模型名称 (如 gpt-4o-2024-11-20)"
  echo "  project    - 项目名称 (可选)"
  exit 1
fi

TYPE="$1"
MODEL_NAME="$2"
shift
shift

if [ $# -eq 0 ]; then
  PROJECTS=('commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR')
else
  PROJECTS=("$@")
fi

for project in "${PROJECTS[@]}"
do
    echo "Translating types for $project"
    python3 src/type_resolution/translate_type.py --project_name=$project --model_name=$MODEL_NAME --type=$TYPE
done
