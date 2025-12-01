lst = [0] * 1600000000
count = 0
for n in range(1550000000):
    lst[n] = lst[n // 10] + n % 10
for n in range(765432015, 1542613239 + 1):
    if lst[n] > lst[n + 1]:
        count += 1
print(count)