# -*- coding:utf-8 -*- 
# Author: Zichuan Wang
# Last Update: 5/1/2014

import re
from nltk.corpus import wordnet as wn
from senti_classifier.senti_classifier import synsets_scores

def calculate_score(word, pos):

    if word == 'EMO_HAPPY':
        return 1.
    elif word == 'EMO_SAD':
        return -1.

    if not re.match('^\w+$', word):
        return 0

    if pos.startswith('NN'):
        pos = 'n'
    elif pos.startswith('VB'):
        pos = 'v'
    elif pos.startswith('RB'):
        pos = 'r'
    elif pos.startswith('JJ'):
        pos = 'a'
    else:
        return 0

    synsets = wn.synsets(word, pos)
    if not synsets:
        return 0
    result = synsets_scores[synsets[0].name]
    neg_score = result['neg'] * -1
    pos_score = result['pos']
    if neg_score == 0:
        return pos_score
    elif pos_score == 0:
        return neg_score 
    else:
        return (neg_score + pos_score) / 2