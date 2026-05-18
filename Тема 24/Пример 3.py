line = open("Пример 3.txt").read()

left = 0
right = 0

max_len = 0
max_seq = ''
last_minus_pos = -1

while right < len(line):
    c = line[right]

    if c not in '01234567*-':
        left = right + 1
        last_minus_pos = -1
    elif c in '*-' and right > left and line[right - 1] in '*-':
        left = right + 1
        last_minus_pos = -1
    elif c == '*' and last_minus_pos >= left:
        left = last_minus_pos + 1
        last_minus_pos = -1
    else:
        if c == '-':
            last_minus_pos = right
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
            max_seq = line[left:right + 1]
    right += 1

max_seq = max_seq.strip('-*')
print(max_seq, len(max_seq))