import pymorphy2 as pm
# from tqdm import tqdm

morph = pm.MorphAnalyzer()

def getNouns(wordArray):
    nouns = []
    for word in wordArray:
        p = morph.parse(word)[0]

        if p.tag.POS == 'NOUN':
            nouns.append(p.normal_form)
            # nouns.append(p.word)
    
    return nouns

def normalize(word):
    return morph.parse(word)[0].normal_form