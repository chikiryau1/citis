import text as t
import morphAnalyze as m
import numpy as np
import math
from hopfield import Hopfield
import slog as s


def frequencyVector(arr):
    '''
        arr: lsit of nouns
        returns: list of lists (list[0] - words, list[1] - counts)
    '''
    uniqWords = np.full((1), arr[0])
    uniqWordCounts = np.full((1), 1)
    
    # N = len(arr)
    # worst case: O(N^2)
    for i in range(1, len(arr)):
        # n = len(uniqWords) worst case: n == i
        # S = (1+N)*N/2
        t = np.where(uniqWords == arr[i])[0]
        isIn = len(t)
        # isIn = 0 | 1 (if 0 => word isn't in uniqWords so need to add one, else need to get words index)

        if len(uniqWords) != len(uniqWordCounts):
            print('miss  ' + str(len(uniqWords)) + '  ' + str(len(uniqWordCounts)))
            break

        if isIn == 0:
            uniqWords = np.append(uniqWords, arr[i])
            uniqWordCounts = np.append(uniqWordCounts, 1)
        else:
            uniqWordCounts[t[0]] += 1
    
    #print(uniqWords, uniqWordCounts)
    return [uniqWords, uniqWordCounts]


def matchMatrix(words, sentences):
    '''
        words: list of uniq words
        sentences: list of sentences
        returns: numpy array with shape words*words
    '''
    matrix = np.zeros((len(words), len(words)))
    for s in sentences:
        ws = t.textToWords(s)
        w = m.getNouns(ws)
        for i in range(len(w)):
            for j in range(len(w)):
                if j == i:
                    continue
                else: 
                    matrix[i][j] += 1
    
    return matrix


def showResults(vector, words):
    keywords = []
    for i in range(len(vector)):
        if abs(vector[i]) > 0.1:
            keywords.append(words[i])
    
    return keywords


def main():
    text = t.poemToProse(t.getText('texts/wiki1.txt'))
    words = t.textToWords(text)
    # print(len(words))
    uniq = frequencyVector(m.getNouns(words))
    print(uniq[0], uniq[1])
    matrix = matchMatrix(uniq[0], t.textToSenteces(text))
    #print(np.linalg.det(matrix))
    # print(np.linalg.svd(matrix)[2][8])
    # print(matrix[2].sum())
    #print(np.linalg.det(matrix_shit))
    # print(np.linalg.det(matrix - np.identity(matrix.shape[0])))
    # print(np.linalg.eigvals(matrix_shit))
    hopfield = Hopfield(matrix, uniq[1])
    hopfield.train()

    # print(hopfield.result)

    print(showResults(hopfield.result, uniq[0]))
    # print(showResults(np.linalg.svd(matrix)[2][8], uniq[0]))

    # for i in range(0, 5):
    #     print(s.second())


main()
