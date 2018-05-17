jupyter nbconvert --to markdown --template=hidecode.tpl Proposal.ipynb

pandoc -s Proposal.md --filter pandoc-citeproc --no-highlight --listings --number-sections -o Proposal.pdf
