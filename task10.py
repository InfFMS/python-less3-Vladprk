# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".
n = int(input())
min_a = 10*100
max_a = -10*100
b = False
for i in range(n):
    a = int(input())
    delit = 0
    for j in range(1, a+1):
        if a % j == 0:
            delit += 1
    if delit == 2:
        b = True
        if max_a < a:
            max_a = a
        if min_a > a:
            min_a = a
if b:
    print('Максимальное:', max_a)
    print('Минимальное:', min_a)
else:
    print('нет')
