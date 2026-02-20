#!/bin/bash

# 用法: bash scripts/generate_test_invocation_map.sh <suffix> [project1] [project2] ...

if [ $# -lt 1 ]; then
  echo "Usage: $0 <suffix> [project_name1] [project_name2] ..."
  exit 1
fi

suffix="$1"
shift

if [ $# -eq 0 ]; then
  PROJECTS=('commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR')
else
  PROJECTS=("$@")
fi

for project in "${PROJECTS[@]}"
do
    echo "Extracting test map for $project"
    python3 src/static_analysis/create_test_method_map.py --project_name=$project --suffix=$suffix
done
