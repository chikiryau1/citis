import re


def getText(path):
    f = open(path)
    return f.read()


def textToSenteces(text):
    return text.split('.')


def textToWords(text):
    return re.split(r'\W+', text)


def poemToProse(s):
    return s.replace('\n', '')