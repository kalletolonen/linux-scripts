#!/bin/bash

# Check if a JSON file was passed as an argument
if [ $# -eq  0 ]; then
    echo "Please provide a JSON file as an argument."
    exit  1
fi

json_file="$1"

# Use jq to parse the JSON and extract the OIDs into an array
oids=$(jq -r '.oidt[]' "$json_file")


base_url="thisismyurl?oid="

declare -a results=()

for oid in $oids; do
    response=$(curl "$base_url$oid")
    
    results+=$response
    
done

echo "$results" > output.json

