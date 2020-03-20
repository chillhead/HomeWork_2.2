import random
class Animals:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        return "Вы покормили %s и довольны :-)" % (self.name)

class Livestock(Animals):
    def to_milk(self):
        return "%s подоена и дала: %s л. молока" % (self.name, {random.randint(1, 10)})

class Birds(Animals):
    def pick_eggs(self):
        return "%s снесла вам яиц: %s шт." % (self.name, {random.randint(1, 10)})

class Goose(Birds):
    def voice(self):
        print("Га-га-га!")

class Cow(Livestock):
    def voice(self):
        print("Муу!")

class Sheep(Animals):
    def shave_off(self):
        return "%s острижен, он дал: %s кг. шерсти" % (self.name, {random.randint(1, 10)})
    def voice(self):
        print("Беее!")

class Hen(Birds):
    def voice(self):
        print("Куд-кудах!")

class Goat(Livestock):
    def voice(self):
        print("Меее!")

class Duck(Birds):
    def voice(self):
        print("Я вас категорически приветствую!")


goose1 = Goose('Серый', 3)
goose2 = Goose('Белый', 4)
cow = Cow('Манька', 300)
sheep1 = Sheep('Барашек', 30)
sheep2 = Sheep('Кудрявый', 70)
hen1 = Hen('Ко-ко', 2)
hen2 = Hen('Кукареку', 3)
goat1 = Goat('Рога', 35)
goat2 = Goat('Копыта', 38)
duck = Duck('Кряква', 2)

print(hen1.pick_eggs())
print(cow.feed())
print(goat1.to_milk())
print(sheep1.shave_off())
duck.voice()

dict = {'gooose1': goose1.weight, 'goose2': goose2.weight, 'cow': cow.weight, 'sheep1': sheep1.weight, 'sheep2': sheep2.weight, 'hen1': hen1.weight, 'hen2': hen2.weight, 'goat1': goat1.weight, 'goat2': goat2.weight, 'duck': duck.weight}
print(sum(dict.values()))
max_weight = int(max(dict.values()))

#print(max_weight)
def get_name_max_weight(dict, value):
    for k, v in dict.items():
        if v == value:
            return k
print(get_name_max_weight(dict, max_weight))

