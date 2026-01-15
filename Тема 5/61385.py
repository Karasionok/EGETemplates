for n in range(1, 10000):
    n = 48611113
    n2 = bin(n)[2:]
    ost = bin(n % 3)[2:]
    n2 += ost.zfill(2)
    ost = bin(n % 5)[2:]
    n2 += ost.zfill(3)
    total = int(n2, 2)
    # print(total)

n = 1222222256
count = 1
while n <= 1555555627:
    count += 1
    n += 32
print(count)