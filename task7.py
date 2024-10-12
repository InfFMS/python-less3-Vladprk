min_f = 1000000000000
b = False
max_a = -10**100
f1, f2 = 1, 1
num = []
a = int(input())
while a != 0:
    num.append(a)
    if max_a < a:
        max_a = a
    a = int(input())
fib = [1, 1]
while fib[-1] < max_a:
    fib.append(fib[-2]+fib[-1])
for i in range(len(num)):
    if num[i] in fib:
        b = True
        if min_f > num[i]:
            min_f = num[i]
if b:
    print('Миниальное из чисел фибоначи:', min_f)
else:
    print('нет')
