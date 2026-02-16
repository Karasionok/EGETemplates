from re import *

text = open('Пример 1.txt').read()

# print(findall(r'', text))

parts = sub(r'[*+]{2,}', ' ', text).split()
max_str = 0
for part in parts:
    if len(sub(r'[+*]', ' ', part).split()) < 41:
        if len(part) > max_str:
            max_str = len(part)
            print(part)
print(max_str)
