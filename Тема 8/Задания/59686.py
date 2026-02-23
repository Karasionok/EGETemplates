import itertools

# АГМНСТУ
total = ''
alf_r = 'УТСНМГА'
alf_begin_r = 'ТСНМГА'
lst = list(itertools.product(alf_begin_r, alf_r, alf_r, alf_r, alf_r, alf_r))
for i in lst:
    word = ''.join(i)
    if word.count('М') == 2 and word.count('Г') <= 1:
        total = word
        break

alf = 'АГМНСТУ'
lst = list(itertools.product(alf, alf, alf, alf, alf, alf))
print(lst.index(tuple(total)) + 1)
