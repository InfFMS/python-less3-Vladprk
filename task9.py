# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".
n = int(input())
min_a = 10*100
max_a = -10*100
b = False
for i in range(n):
    a = int(input())
    if 100 > a > 9 and a % 3 == 0:
        b = True
        if min_a > a:
            min_a = a
        if max_a < a:
            max_a = a
if b:
    print('Максимальное:', max_a)
    print('Минимальное:', min_a)
else:
    print('нет')
