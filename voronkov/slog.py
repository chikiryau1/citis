from random import randint

g = ['а', 'у', 'о', 'ы', 'и', 'э', 'е']
s = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш']

def gen():
    word = ''
    for i in [0,1,2]:
        word += s[randint(0, len(s) - 1)]
        word += g[randint(0, len(g) - 1)]
        if randint(0, 10) > 6:
            word += s[randint(0, len(s) - 1)]

    return word

def second():
    word = gen()
    
    if word[-1] in g:
        word += 'вич  матрас'
    else: 
        word += 'ич  матрас'

    return word