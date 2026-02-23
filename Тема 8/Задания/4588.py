import itertools

alf = sorted('МУХА')

lst = list(itertools.product(alf, repeat=4))
print(lst.index(tuple('ХУХХ')) + 1)

