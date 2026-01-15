for i in range(1000):
    n = i
    n3 = ''
    while n > 0:
        n3 += str(n % 3)
        n //= 3
    n3 = n3[::-1]
    if i % 3 == 0:
        n3 = '1' + n3 + '02'
    else:
        s = 4 * (i % 3)
        s3 = ''
        while s > 0:
            s3 += str(s % 3)
            s //= 3
        s3 = s3[::-1]
        n3 += s3
    total = int(n3, 3)
    if total <= 250:
        print(i)