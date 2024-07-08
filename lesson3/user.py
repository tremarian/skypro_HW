class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printName(self):
        print(f'Мое имя {self.first_name}')

    def printLName(self):
        print(f'Моя фамилия {self.last_name}')

    def printNameLName(self):
        print(f'Мое имя {self.first_name} и фамилия {self.last_name}')
