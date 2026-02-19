#!/bin/bash

# 用法: bash scripts/decompose_test.sh [project1] [project2] ...
# 示例:
#   bash scripts/decompose_test.sh maven
#   bash scripts/decompose_test.sh commons-cli maven

if [ $# -eq 0 ]; then
  echo "Usage: $0 <project_name> [project_name2] ..."
  echo ""
  echo "Arguments:"
  echo "  project_name - 项目名称 (可多个)"
  echo ""
  echo "Examples:"
  echo "  $0 maven"
  echo "  $0 commons-cli maven commons-codec"
  exit 1
fi

for project in "$@"
do
    echo "Decomposing tests for $project";
    mkdir -p java_projects/cleaned_final_projects_decomposed_tests/$project;
    cp -r java_projects/cleaned_final_projects/$project java_projects/cleaned_final_projects_decomposed_tests/;
    python3 src/static_analysis/decompose_dev_test.py --project_name=$project;
done
