#!/usr/bin/env bash

llm "Write a mermaid chart for this code" < <(tree $1 && find $1 -type f \( -name "*.md" -o -name "*.py" -o -name "*.html" -o -name "*.js" -o -name "*.scss" -o -name "*.yaml" -o -name "*.tsx" \) -not -path "*/node_modules/*" -not -path "*/.git/*" -not -path "*/.venv/*" -print0 | while IFS= read -r -d '' file; do
  echo -e "\n=== $file ===\n"
  cat "$file"
done)

