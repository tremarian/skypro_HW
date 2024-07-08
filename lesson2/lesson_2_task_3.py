def square():
    a = float(input('Введите сторону квадрата: '))

    if a != int(a):
        a = int(a) + 1

    s = a*a
    print(f"Площадь квадрата: {s}")


square()
