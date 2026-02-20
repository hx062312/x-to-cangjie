#!/bin/bash

# 用法: bash scripts/create_skeleton.sh <suffix> [project1] [project2] ...
# 示例:
#   bash scripts/create_skeleton.sh "_decomposed_tests" maven

if [ $# -lt 1 ]; then
  echo "Usage: $0 <suffix> [project_name1] [project_name2] ..."
  echo ""
  echo "Arguments:"
  echo "  suffix      - 后缀 (如 _decomposed_tests)"
  echo "  project     - 项目名称 (可选，默认全部)"
  exit 1
fi

suffix="$1"
shift

if [ $# -eq 0 ]; then
  PROJECTS=('commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR')
else
  PROJECTS=("$@")
fi

pwd=$(pwd)

# 默认模型列表
MODELS=('deepseek-coder-33b-instruct' 'gpt-4o-2024-11-20')

for model in "${MODELS[@]}"; do
    for type in 'body'; do
        for temperature in 0.0; do
            for project in "${PROJECTS[@]}"; do
                echo "Creating skeleton for $project"
                export PYTHONPATH=$pwd/data/skeletons/$project
                python3 src/static_analysis/create_skeleton.py --project_name=$project --model_name=$model --type=$type --suffix=$suffix --temperature=$temperature
            done
        done
    done
done
