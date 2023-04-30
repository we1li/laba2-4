import sys

if __name__ == '__main__':
    print("Введите 10 элементов: ")
    A = list(map(int, input().split(" ")))
    new_list = A
    if not A:
        print("Заданный список пустой", file=sys.stderr)
        exit(1)

    f=0
    n=1
    k=[]
    for i in A:
        if i % 3 == 0:
            f += 1
            n *= i
            k.append(i)
    print("Количество элементов кратное 3 = ", f)
    print("Произведение новых элементов = ", n)
    print(k)
    