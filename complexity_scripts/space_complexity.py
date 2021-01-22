# general
import numpy as np
import time

# models
from danlp.models import load_bert_ner_model, load_flair_ner_model

# dataset
from danlp.datasets import DDT

# utils
from flair.data import Sentence, Token
from copy import deepcopy
from memory_profiler import profile

# load models
bert = load_bert_ner_model()
flair = load_flair_ner_model()

# get data (splitted into a training set, a validation set, and a test set)
ddt = DDT()
train, valid, test = ddt.load_as_simple_ner(True)

# divide the observations and the targets of the testset into new variables
sentences, categories = test

@profile
def get_bert_predictions(sentences):
    predictions = []

    '''for sentence in sentences:
        predictions.append(bert.predict(sentence)[1])'''
    pred = bert.predict(sentences[0])

    predictions.append(pred[1])

    predictions.append(bert.predict(sentences[1])[1])
    predictions.append(bert.predict(sentences[2])[1])
    predictions.append(bert.predict(sentences[3])[1])

    return predictions

bert_preds = get_bert_predictions(sentences)

@profile
def get_flair_predictions(sentences):
    predictions = []
    
    flair_sentences = []
    for sentence in sentences:
        flair_sentence = Sentence()
        for token in sentence:
            flair_sentence.add_token(Token(token))
        flair_sentences.append(flair_sentence)
    flair.predict(flair_sentences)
    
    for s in flair_sentences:
        predicted_categories = []
        for t in s:
            predicted_categories.append(t.tags['ner'].value)
        predictions.append(predicted_categories)
    
    return predictions

#flair_preds = get_flair_predictions(sentences)