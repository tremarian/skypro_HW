from smartphone import Smartphone

catalog = [
    Smartphone('brand0', 'model0', '+79000000000'),
    Smartphone('brand1', 'model1', '+79000000001'),
    Smartphone('brand2', 'model2', '+79000000002'),
    Smartphone('brand3', 'model3', '+79000000003'),
    Smartphone('brand4', 'model4', '+79000000004')
    ]


for y in range (0,5):
    print(f'<{catalog[y].brand}> - <{catalog[y].model}>. <{catalog[y].number}>')