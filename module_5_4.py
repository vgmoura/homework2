class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        house_history = args[0]
        cls.houses_history.append(house_history)
        return super ().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Наименование:{self.name} Колличество этажей:{self.number_of_floors}'

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# переопределение метода __del__(self) в котором будет выводится строка '... снесён, но он останется в истории'

del h2
del h3

print(House.houses_history)
