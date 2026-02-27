#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: ./scripts/java/reduce_third_party_libs.sh <project_name>"
  exit 1
fi

PROJECT_NAME="$1"

python3 ./src/java/preprocessing/reduce_third_party_libs.py "$PROJECT_NAME"



