def bank(x,y):
    for n in range (0,y):
        x = x + (x / 100 * 10)
    print(f"Сумма накоплений: {x}")
x = int(input("Введите сумму вклада: "))
y = int(input("Введите срок вклада в годах: "))
bank(x,y)