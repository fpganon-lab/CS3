class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self) -> str:
        raise NotImplementedError("Subclasses must implement this method.")

    def feed(self) -> str:
        raise NotImplementedError("Subclasses must implement this method.")

class Lion(Animal):
    def make_sound(self) -> str:
        return f"{self.name} roars loudly!"

    def feed(self) -> str:
        return f"{self.name} eats fresh meat."


class Elephant(Animal):
    def make_sound(self) -> str:
        return f"{self.name} trumpets!"

    def feed(self) -> str:
        return f"{self.name} eats grass and fruits."


class Monkey(Animal):
    def make_sound(self) -> str:
        return f"{self.name} chatters!"

    def feed(self) -> str:
        return f"{self.name} eats bananas."



lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())      
print(lion.feed())
print("------")

print(elephant.make_sound())
print(elephant.feed())
print("------")

print(monkey.make_sound())
print(monkey.feed())
print("------")