---
# See https://pandoc.org/MANUAL.html#variables-for-latex

title: An exploration into the use of Natural Language Processing in Stock Market Prediction on the JSE

author:
- Robert Brink
- Marcus Gawronsky
- Christopher Kleyweg

date: 16 March 2018

number_sections: true
secnumdepth: 1
pagenumbering: true

papersize: a4
#fontfamily: Latin Modern

biblio-title: Bibliography   
bibliography: ../../library.bib
csl: ./harvard-university-of-cape-town.csl

exclude_output: true
exclude_input: true
exclude_input_prompt: true
exclude_output_prompt: true
exclude_markdown: False
exclude_code_cell: true
---
# Introduction
According to the Efficienct Market Hypothesis markets take into account all relevent information in efficiently pricing securities [@Samuelson1965].  While many studies have explored this supposition under its strong, semi-strong and weak form, the growing volume, velocity and variety of market data has forced financiers to invest more-and-more in technology as a tool for decision making.  

Investors form a mosaic of information pulling from financial reports, news articles and price data.  With the growing trend towards automated trading a requirement to explore new forms of unstructured and semi-structured data in order to remain competitive has emerged.  This research aims to explore the use of text data in quantitative stock price prediction.  

# Brief Literature Review
Natural Language Processing (NLP) is a complex challenge in feature extraction and model building.  Many techniques represent a trade-off between computability and complexity, sacrificing elements of speech such as word order, conjugation and meaning.  Even small corpuses can contain hundreds-of-thousands of unique words.  Reducing this dimensionality whilst capturing the sentiment and meaning of documents is a broad and long-standing research area in the fields of computer science and statistical research.  Dominant in this literature is document vector representations such as the bag-of-words approach, in which documents are stripped of features such as punctation, capitallization and word conjugates and represented as a vector counting the occurance of each word in the document. 
  
Recent conference preceedings from the 11th International Workshop on Semantic Evaluation Cortis2017 summarise the work of 31 research teams with the task of performing fine-grained sentiment analysis on financial micro-blogs and news.  In this work one can observe a blossoming of new techniques from works published only a few years earlier.  The emergence of new tools such as Latent Sentiment Analysis, Convolutional Neural Networks and Doc2Vec for document vector extraction demonstrates the potential in revisiting such research in this area. These tools can be used in conjunction with new models from the field of Machine Learning such Naive Bayes, Random Forest and Artificial Neural Networks [@Lea, @Blei2003, @Johnson2014].  
  
While many papers focus on the predictive power of natural language in stock market prediction questions remain on the temporal impact of this data on stock prices.  @Gidofalvi2001b demonstrates a clear 20-minute lead and lag window around news articles where price response is observed - indicating an important dimension to the problem.  

In a review of some 262 natural language and readility studies in the field of Accounting, Auditing and Finance, @OLeary2009 identified narrative disclosures as untapped repositories of qualitative data key in stock price prediction.  
  
Currently little research has been done on narrative disclosures and South African data in the field of NLP stock prediction.  This research aims to bridge this gap using a corpus of news articles and JSE SENS (Stock Exchange News Service) data  implementing modern tachniques in the analysis. 

# Approach
Data for this project will comprise of articles scraped from publically avalible news services.  This data contains information on the source, time of publishing, a title and the article itself.  

This project aims to compare the use of various vector representations and embeddings for Natural Langauge Processing. These include the use of Bag-of-Words, N-gram and continuous vector representations [@Mikolov2013].  This research will take an event-based approach and compare the use of Random Forest, Naive Bayes and Kernel Support Machine Models.  

# Conditions and risk analysis
This project will require access to the University of Cape Town's High Performance Computing facilities due to the size and complexity of the models estimated. 

# Referrences
