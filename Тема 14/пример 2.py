alf = '0123456789' + 'ABCDEFGHIJK'
for x in alf:
    n1 = int('98' + x + '79641', 22)
    n2 = int('25' + x + '49', 22)
    n3 = int('63' + x + '5', 22)
    total = n1 + n2 + n3
    if total % 21 == 0:
        print(total / 21)
        break