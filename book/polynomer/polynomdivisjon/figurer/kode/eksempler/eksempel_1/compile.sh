#!/bin/bash

# Check if an argument was provided
if [ $# -eq 0 ]; then
    echo "No arguments provided. Usage: ./compile_tex.sh [Name]"
    exit 1
fi

# Create a new .tex file based on the template
cp template.tex temp.tex

# Replace the placeholder with the actual name passed as the first argument
sed -i "s/\\VARNAME/$1/g" temp.tex

# Compile the LaTeX document
pdflatex temp.tex

# Clean up (optional)
rm temp.tex temp.aux temp.log