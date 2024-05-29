def is_year_leap(num):
    if num % 4 == 0:
        return print('True')
    else:
        return print('False')


def get_year():
    year = int(input('Введите год: '))
    print(f"{year} : ", end='')
    is_year_leap(year)

get_year()