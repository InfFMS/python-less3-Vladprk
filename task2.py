# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено двузначных натуральных чисел,
# и сколько других.
count = 0
count1 = 0
a = int(input())
while a != 0:
    count += 1
    if a//100 == 0 and a//10 > 0:
        count1 += 1
    a = int(input())
print(count1)
print(count - count1)
