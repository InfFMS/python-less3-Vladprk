# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, среднее арифметическое тех введённых чисел,
# которые являются степенями числа 2.
# Вывести "нет", если таких чисел нет.
count = 0
summ = 0
a = int(input())
while a != 0:
    b = False
    for i in range(1, a + 1):
        if 2**i == a:
            b = True
    if b:
        count += 1
        summ += a
    a = int(input())
if count > 0:
    print(summ/count)
else:
    print('нет')
