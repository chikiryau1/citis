import os
import numpy as np
import re


def create_vocabulary(sentences, r=2):
    vocabulary = {}
    draft_vocabulary = {}

    for sentence in sentences:
        for word in sentence:
            if word in draft_vocabulary:
                draft_vocabulary[word] += 1
            else:
                draft_vocabulary.update({word:1})
    value = 0
    for key in draft_vocabulary:

        if draft_vocabulary[key] > r:
            vocabulary.update({key: value})
            value += 1
    del draft_vocabulary
    return vocabulary


def create_corpus_matrix(sentences, vocabulary, window=2):
    def if_in_vocabulary(word, context):
        if word in vocabulary and context in vocabulary:
            return True
        return False

    n = len(vocabulary)
    corpus_matrix = np.zeros((n, n))

    for sentense in sentences:
        for position_of_word in range(len(sentense)):
            for i in range(max(0, position_of_word - window), min(position_of_word + window + 1, len(sentense))):
                word = sentense[position_of_word]
                context = sentense[i]
                if if_in_vocabulary(word, context) and i != position_of_word:
                    corpus_matrix[vocabulary[word]][vocabulary[context]] += 1

    return corpus_matrix


def map_model(vocabulary):
    pass


def init():
    file = open("data/pos.txt", "r")
    doclist = [line for line in file]
    docstr = ''.join(doclist)
    sentences = re.split(r'[.!?]', docstr)
    sentences = [sentence.split() for sentence in sentences if len(sentence) > 1]
    vocab = create_vocabulary(sentences)
    print(vocab)
    # D = create_corpus_matrix(sentences, vocab)


if __name__ == "__main__":
    init()
