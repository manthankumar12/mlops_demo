#!/bin/bash
 
# Extract source code from YAML file
SOURCE_CODE=$(cat your_file.yml | grep 'source_code' | cut -d ':' -f 2-)
 
# Trim leading and trailing whitespaces
SOURCE_CODE=$(echo "$SOURCE_CODE" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
 
# Save the extracted source code to a temporary file
echo "$SOURCE_CODE" > extracted_code.txt 
