from address import Address
from mailing import Mailing

to = Address(644014, 'Омск', 'ул. 1 Мая', 'д. 2', 'кв. 1')
fr = Address(183036, 'Мурманск', 'ул. Кильдинская', 'д. 4', 'кв. 15')


shiping = Mailing(to, fr, 320, '№1')

shiping.addFrom(fr)
shiping.addTo(to)

print(f'Отправление {shiping.track} из ', end="")
shiping.getFrom().printAddress()
print(' - ', end="")
shiping.getTo().printAddress()
print(f'. Стоимость {shiping.cost} рублей')