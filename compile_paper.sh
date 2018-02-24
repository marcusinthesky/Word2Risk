jupyter nbconvert --to markdown --template=hidecode.tpl Import_Data.ipynb

pandoc -s Import_Data.md --filter pandoc-citeproc --no-highlight --strip-comments --listings --number-sections -o paper.pdf

