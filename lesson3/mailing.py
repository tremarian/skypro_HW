class Mailing:

    def __init__(self, addres_to, adress_from, cost, track):
        self.to_address = addres_to
        self.from_address = adress_from
        self.cost = cost
        self.track = track

    def printTo(self):
        print(self.to_address)

    def printFrom(self):
        print(self.from_address)

    def printCost(self):
        print(self.cost)

    def printTrack(self):
        print(self.track)

    def addFrom(self, addres_from):
        self.addres_from = addres_from

    def getFrom(self):
        return self.addres_from

    def addTo(self, addres_to):
        self.addres_to = addres_to

    def getTo(self):
        return self.addres_to
