number = 2 * 729 ** 2014 + 2 * 81 ** 2018 + 2 * 27 ** 2020 - 2 * 9 ** 2022 - 2024
z = 27
count = 0
while number > 0:
    if number % z > 9:
        count += 1
    number //= z
print(count)