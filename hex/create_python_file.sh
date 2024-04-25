#!/bin/bash
 
# Read the extracted source code from the temporary file
SOURCE_CODE=$(cat extracted_code.txt)
 
# Write the source code to a Python file
echo "$SOURCE_CODE" > output.py
