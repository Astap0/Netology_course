class Animal:
    def __init__(self, weight, name: str = "") -> None:
        self.name = name
        self.weight = weight

    def _get_sound(self):
        raise NotImplementedError

    def speak(self):
        sound = self._get_sound()
        print(f"{self.name} is says {sound}")

    def feed(self):
        print(f"You fed {self.name}!")


class Ruminant(Animal):
    def __init__(self, weight, name: str = "") -> None:
        super().__init__(weight, name)

    def milking(self):
        print(f"You are milking {self.name}")


class Bird(Animal):
    def __init__(self, weight, name: str = "") -> None:
        super().__init__(weight, name)

    def collect_eggs(self):
        print(f"You are collect {self.name}`s eggs")


class Goose(Bird):
    def __init__(self, weight, name: str = "") -> None:
        super().__init__(weight, name)

    def _get_sound(self):
        return "Gagagaga"


class Duck(Bird):
    def __init__(self, weight, name: str = "") -> None:
        super().__init__(weight, name)

    def _get_sound(self):
        return "Quack-quack"


class Chicken(Bird):
    def __init__(self, weight, name: str = "") -> None:
        super().__init__(weight, name)

    def _get_sound(self):
        return "Cluck"


class Cow(Ruminant):
    def __init__(self, weight, name: str = "") -> None:
        super().__init__(weight, name)

    def _get_sound(self):
        return "Moooooo"


class Goat(Ruminant):
    def __init__(self, weight, name: str = "") -> None:
        super().__init__(weight, name)

    def _get_sound(self):
        return "Beaaaa"


class Sheep(Animal):
    def __init__(self, weight, name: str = "") -> None:
        super().__init__(weight, name)

    def sheare(self):
        print(f"You are shearing {self.name} the sheep!")

    def _get_sound(self):
        return "Baaaa"


pet_1 = Goose(4, "Grey")
pet_2 = Goose(5, "White")
pet_3 = Cow(500, "Manka")
pet_4 = Sheep(70, "Barashek")
pet_5 = Sheep(75, "Kudriaviy")
pet_6 = Chicken(2, "Co-Co")
pet_7 = Chicken(3, "Kukareku")
pet_8 = Goat(60, "Roga")
pet_9 = Goat(65, "Kopita")
pet_10 = Duck(3, "Karkva")

my_pets = [pet_1, pet_2, pet_3, pet_4, pet_5, pet_6, pet_7, pet_8, pet_9, pet_10]
weight_list = []
weight_sum = int()
for pet in my_pets:
    pet.feed()
    pet.speak()
    weight_list.append(pet.weight)
for i in weight_list:
    weight_sum += i
print(f"Sum weight is {weight_sum}kg")
pet_1.collect_eggs()
pet_2.collect_eggs()
pet_3.milking()
pet_4.sheare()
pet_5.sheare()
pet_6.collect_eggs()
pet_7.collect_eggs()
pet_8.milking()
pet_9.milking()
pet_10.collect_eggs()
