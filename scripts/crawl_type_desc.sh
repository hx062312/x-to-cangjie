#!/bin/bash

# 用法: bash scripts/crawl_type_desc.sh [project1] [project2] ...

if [ $# -eq 0 ]; then
  PROJECTS=('commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR')
else
  PROJECTS=("$@")
fi

for project in "${PROJECTS[@]}"
do
    echo "Crawling type description for $project"
    python3 src/type_resolution/crawl_type_desc.py --project_name=$project
done
