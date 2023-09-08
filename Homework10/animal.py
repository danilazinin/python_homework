class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


class Factory:
    def __init__(self, animal_class, **kwargs):
        self.animal = animal_class
        self.params = kwargs

    def make_animal(self):
        params = list(item for item in self.params.values())
        if self.animal == str(self.animal).lower():
            return Bird(*params)
        elif self.animal == str(self.animal).lower():
            return Reptiles(*params)
        else:
            return Fish(*params)


class Fish(Animal):

    def __init__(self, name, age, color, fins_count):
        super().__init__(name, age, color)
        self.fins_count = fins_count

    def show_special_attributes(self):
        print(self.fins_count)


class Bird(Animal):

    def __init__(self, name, age, color, can_fly=True):
        super().__init__(name, age, color)
        self.flying = can_fly

    def show_special_attributes(self):
        print(f'can fly = {self.flying}')


class Reptiles(Animal):

    def __init__(self, name, age, color, body_size):
        super().__init__(name, age, color)
        self.size = body_size

    def show_special_attributes(self):
        print(f'length of body = {self.size}')


factory = Factory('bird', name='sd', age=9, color='green', d=False)
animal = factory.make_animal()
print(animal.age)