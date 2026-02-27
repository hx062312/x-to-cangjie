#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: ./scripts/java/decompose_test.sh <project_name>"
  exit 1
fi

PROJECT_NAME="$1"

echo "Decomposing tests for $PROJECT_NAME";
mkdir -p projects/java/cleaned_final_projects_decomposed_tests/$PROJECT_NAME;
cp -r projects/java/cleaned_final_projects/$PROJECT_NAME projects/java/cleaned_final_projects_decomposed_tests/;
python3 src/java/static_analysis/decompose_dev_test.py --project_name=$PROJECT_NAME;

done