from address import Address
from mailing import Mailing

mike = Address(1, 2, 3, 4, 5)
bob = Address(1, 2, 3, 4, 5)
new = Mailing(mike, bob, 1, 1 )

print(new)