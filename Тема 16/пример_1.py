lst = [0] * 6 * 10 ** 7
count = 0
for n in range(6 * 10 ** 7):
    if n % 2 == 0:
        lst[n] = lst[n // 10] + n % 10
    else:
        lst[n] = lst[n // 10]
for n in range(10 ** 7, 6 * 10 ** 7):
    if lst[n] == 0:
        count += 1
print(count)