import numpy as np
import pandas as pd

from sklearn.base import TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances

from gensim.models.word2vec import Word2Vec

class WeightedWordVectors(TransformerMixin):
    """    
    Libraries & Versions:
    Python==3.6.5
    Pandas=='0.23.1' as pd
    nltk=='3.3'
    numpy=='1.14.5'
    
    Keyword arguments:
    X -- Pandas Series of text as strings
    """
    def __init__(self, model=None, meta=None, disk=None):
        self.meta = meta
        
        if model == None:
            self.word2vec = Word2Vec(sentences=self.meta.str.split().tolist())
        else:
            self.word2vec =  model
            self.word2vec.train(sentences=self.meta.str.split().tolist())
        
        #Fit TFIDF
        self.tfidf = TfidfVectorizer()
        self.idfs = self.tfidf.fit_transform(self.meta)
        self.inverse_idfs = self.tfidf.inverse_transform(self.idfs)
    
        return self
        
    
    def fit(self, X, y=None, meta=None, P=None):
        #Split into sentences
        for i in X.index:
            self.word2vec.build_vocab(X.loc[i].str.split().tolist(), keep_raw_vocab=True, update=True)
            self.word2vec.model_trimmed_post_training = False
            self.word2vec.min_alpha_yet_reached = False
            self.word2vec.batch_words = X.loc[i].apply(lambda x: len(x.split())).max()
            self.word2vec.train(X.loc[i].str.split().tolist(), 
                           total_examples=X.loc[i].shape[0], start_alpha=0.05, 
                           end_alpha=0.01, epochs=1, compute_loss=True)
            
            disk.append( (euclidean_distances(self.transform(self, meta)) @ P).sum(1) )
            
        return self

    def transform(self, meta):        
        #Weighted Vectors
        weighted_docs = []        
        for idf, inv in zip(self.idfs, self.inverse_idfs):
            try:
                weight = idf[idf!=0]
                vector = self.word2vec[inv]
                weighted_doc = weight.dot(vector)
            except:
                weighted_doc = np.empty((1, 300), np.float64)    
            weighted_docs.append(weighted_doc.tolist()[0])
                
        return pd.DataFrame(weighted_docs).fillna(0)
        
    '''