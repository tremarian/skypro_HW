class Address:

    def __init__(self, index, city, street, house, flat):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def printAddress(self):
        print(
            self.index, self.city, self.street, self.house, self.flat,  end=""
            )
