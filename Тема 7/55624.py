I_book = 1 * 1024
v = 1.5
t = (I_book / v) * 60
print(t)
I = 2 * 48000 * 24 * t / 8 / 1024
I_total = I * 0.16
n = I_total / (15 * 1024)
print(n)