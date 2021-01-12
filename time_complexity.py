# general
import numpy as np
import time
import torch

# models
from danlp.models import load_bert_ner_model#, load_flair_ner_model

# dataset
from danlp.datasets import DDT

# utils
#from flair.data import Sentence, Token

# load models
bert = load_bert_ner_model()
'''flair = load_flair_ner_model()'''

# CUDA for PyTorch
use_cuda = torch.cuda.is_available()
device = torch.device("cuda:0" if use_cuda else "cpu")
torch.backends.cudnn.benchmark = True

# get data (splitted into a training set, a validation set, and a test set)
ddt = DDT()
train, valid, test = ddt.load_as_simple_ner(True)

# divide the observations and the targets of the testset into new variables
sentences, categories = test

batch_size = 64

batch_sentences = []

num_sentences = len(sentences)
iterator = 0
while len(batch_sentences) < num_sentences/batch_size:
    stop = batch_size*(iterator+1)
    if stop>num_sentences:
        stop = num_sentences
    batch_sentences.append(sentences[batch_size*iterator:stop])
    iterator += 1

def get_bert_predictions(sentences):
    #sentences = sentences.to(device)
    
    predictions = []
    
    for sentence in sentences:
        predictions.append(bert.predict(sentence)[1])
    
    return predictions

'''def get_flair_predictions(sentences):
    sentences = sentences.to(device)
    
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
'''
# bert
start = time.time()
#bert.model.to(device)
for sents in batch_sentences:
    bert_preds = get_bert_predictions(sents)
bert_time_spent = time.time()-start

print('BERT time:')
print(bert_time_spent)

'''# flair
start = time.time()
flair.to(device)
for sents in batch_sentences:
    flair_preds = get_flair_predictions(sents)
flair_time_spent = time.time()-start

print('FLAIR time:')
print(flair_time_spent)

'''

