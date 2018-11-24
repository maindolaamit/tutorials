import nltk
# nltk.download('punkt')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import re

positive_reviews = BeautifulSoup(
    open('positive.review').read(), features="lxml")
negative_reviews = BeautifulSoup(
    open('negative.review').read(), features="lxml")

positive_reviews = positive_reviews.findAll('review_text')

trigrams_matrix = {}


def update_trigram_matrix(trigram):
    if trigram not in trigrams_matrix.keys():
        trigrams_matrix[trigram] = 1
    else:
        trigrams_matrix[trigram] += 1


pattern = '[^a-zA-z]'
for review_text in positive_reviews:
    line = review_text.text.lower()
    line = re.sub(pattern, ' ', line)
    # print(line)
    tokens = nltk.tokenize.word_tokenize(line)
    if len(tokens) < 3:
        continue

    for i in range(len(tokens) - 2):
        trigram = (tokens[i], tokens[i+1], tokens[i+2])
        update_trigram_matrix(trigram)

df = pd.DataFrame(zip(trigrams_matrix.keys(), trigrams_matrix.values()), columns=[
                  "trigram", "count"])
# print(trigrams_matrix)
print(df.head(5))
