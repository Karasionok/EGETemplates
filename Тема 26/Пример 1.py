f = open('Пример 1.txt')
f.readline()
time = sorted([list(map(int, a.split())) for a in f.readlines()])
time.append([86400000, 86400000])
max_end = 0
no_process = []
for i in time:
    if max_end >= i[0]:
        max_end = max(max_end, i[1])
    else:
        no_process.append(i[0] - max_end)
        max_end = i[1]
print(len(no_process), sum(no_process))