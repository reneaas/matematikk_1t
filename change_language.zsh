#!/bin/zsh

root_dir="./_build/html/book"

find $root_dir -type f -name "*.html" | while read -r file; do
    python change_language.py "$file"
done