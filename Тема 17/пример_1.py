n = [int(a) for a in open('17.txt')]
count = 0
lst = []
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if (n[i] % 15 == 0 or n[j] % 15 == 0) and (n[j] - n[i]) % 60 == 0:
            count += 1
            lst.append(n[j] - n[i])
print(count, max(lst))
