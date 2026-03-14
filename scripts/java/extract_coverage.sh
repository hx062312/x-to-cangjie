#!/bin/bash

# ./scripts/java/extract_coverage.sh simple-calculator _decomposed_tests
# ./scripts/java/extract_coverage.sh commons-fileupload _decomposed_tests

if [ $# -ne 2 ]; then
  echo "Usage: ./scripts/java/extract_coverage.sh <project> <suffix>"
  exit 1
fi

project=$1
suffix=$2
reduced_dir="./projects/java/automated_reduced_projects/$project"

jacoco_plugin=$(cat <<'EOF'
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.10</version>
    <executions>
        <execution>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
        </execution>
        <execution>
            <id>report</id>
            <phase>test</phase>
            <goals>
                <goal>report</goal>
            </goals>
        </execution>
    </executions>
</plugin>
EOF
)

if [ ! -d "$reduced_dir" ]; then
    echo "Error: Project '$project' not found in $reduced_dir."
    exit 1
fi

cd "$reduced_dir" || exit

if [ ! -f "pom.xml" ]; then
    echo "Error: pom.xml not found in $reduced_dir."
    exit 1
fi

# Check if jacoco plugin already exists
if grep -q "jacoco-maven-plugin" pom.xml; then
    echo "JaCoCo plugin already exists in pom.xml"
else
    awk -v config="$jacoco_plugin" '
        /<build>/ { in_build = 1 }
        /<\/build>/ { in_build = 0 }
        in_build && /<plugins>/ {
            print;
            print config;
            next
        }
        { print }
    ' pom.xml > pom.xml.new && mv pom.xml.new pom.xml
    echo "JaCoCo plugin added to pom.xml"
fi

echo "Running mvn clean test -Drat.skip=true..."
mvn clean test -Drat.skip=true

cd - > /dev/null || exit

echo "extracting test coverage for $project"
python3 src/java/static_analysis/extract_source_tests.py --project=$project --suffix=$suffix
