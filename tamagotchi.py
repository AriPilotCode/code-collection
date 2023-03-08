class Animal:
    """
       A class used to represent an animal
        """



    Zoo_name = "Hayaton"

    def __init__(self, name="", hunger=0):
        self._hunger = hunger
        self._name = name


    def get_name(self):
        print(self._name)

    def is_hungry(self):
        return self._hunger > 0

    def feed(self):
        self._hunger -= 1

    def talk(self):
        ""


class Dog(Animal):
    """
       B class used to represent a type of the animal
        """

    def __init__(self, name, hunger):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        super().get_name()

    def is_hungry(self):
        return super().is_hungry()

    def feed(self):
        self._hunger -= 1

    def talk(self):
        return "waff waff".format(super().talk())

    def fetch_stick(self):
        return "There you go, sir!"


class Cat(Animal):

    def __init__(self, name, hunger):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        super().get_name()

    def is_hungry(self,):
        return super().is_hungry()

    def feed(self):
        super().feed()

    def talk(self):
        return "meow"

    def chase_laser(self):
        return "Meeeeow"


class Skunk(Animal):

    def __init__(self, name, hunger, stink_count=6):
        self._name = name
        self._hunger = hunger
        self._stink_count = stink_count

    def get_name(self):
        super().get_name()

    def is_hungry(self,):
        return super().is_hungry()

    def feed(self):
        super().feed()

    def talk(self):
        return "tssss"

    def stink(self):
        return "Dear lord!"


class Unicorn(Animal):

    def __init__(self, name, hunger):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        super().get_name()

    def is_hungry(self,):
        return super().is_hungry()

    def feed(self):
        super().feed()

    def talk(self):
        return "Good Day, darling"

    def sing(self):
        return "I’m not your toy..."


class Dragon(Animal):

    def __init__(self, name, hunger, color="Green"):
        self._name = name
        self._hunger = hunger
        self._color = color

    def get_name(self):
        super().get_name()

    def is_hungry(self,):
        return super().is_hungry()

    def feed(self):
        super().feed()

    def talk(self):
        return "Raaaawr"

    def breath_fire(self):
        return "$@#$#@$"


def main():

    my_zoo_list = [Dog("Brownie", 10), Dog("Doggo", 80), Cat("Zelda", 3), Cat("Kitty", 80), Skunk("Stinky", 0), Skunk("Stinki Jr.", 80), Unicorn("Keith", 7), Unicorn("Clair", 80), Dragon("Lizzi", 1450), Dragon("McFly", 80)]

    for animal in my_zoo_list:

        print(type(animal).__name__, animal._name)
        print(animal.talk())

        if isinstance(animal, Dog):
            print(animal.fetch_stick())

        elif isinstance(animal, Cat):
            print(animal.chase_laser())

        elif isinstance(animal, Skunk):
            print(animal.stink())

        elif isinstance(animal, Unicorn):
            print(animal.sing())

        elif isinstance(animal, Dragon):
            print(animal.breath_fire())

        while animal.is_hungry():
            animal.feed()

    print(Animal.Zoo_name)


if __name__ == "__main__":
    main()

