import sys
print("Введите список: ")
x = list(map(int, input().split(" ")))
a = int(input("Введите a:"))
b = int(input("Введите b:"))
x1 = []
x2=x
k=0
sum=0

if a<0 or b<0:
    print("Введите положительное a/b", file=sys.stderr)
    exit(1)
if a>b:
    print("число не должно быть меньше b", file=sys.stderr)
    exit(1)
for l in x:
    x1.append(abs(float(l)))
m = min(x1)
print("Миимальное число по модулю", m)
for i in x:
    if (k == 0) and (i < 0):
        k+=1
        sum = i
    if (k>0):
        sum += abs(i)
if sum == 0:
    print("В списке нет отрицательных чисел", file=sys.stderr)
else:
    print("Сумма модулей после первого отрицательного чила", sum)
for c in range(len(x)):
    if a<=b:
        x2[a]=0
        a+=1
print("Новый список, где элементы от a и b заменены нулями:")
print(x2)