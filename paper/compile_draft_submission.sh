jupyter nbconvert --to markdown --template=hidecode.tpl Draft\ Submission.ipynb
pandoc -s "Draft Submission.md" --bibliography=./library.bib --csl=harvard-university-of-cape-town.csl --number-sections -o Draft\ Submission.pdf
