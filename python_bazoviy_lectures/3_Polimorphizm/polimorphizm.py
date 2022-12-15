# PLAN UROKA

# Chto takoe polimorphizm.

# POLIMORPHIZM - raznoe povedenie odnogo i togo zhe metoda v raznih classah. Polimorphizm
# dostigaetsya pytem peregruzki ili pereopredeleniya metoda.

# Takim obrazom dostigaetsya dopolnitelnaya gibkost programmi. A takzhe, znachitelno sokrashaetsya
# dublirovanie koda, chto ochen vazhno dlya horoshego i podderzhivaemogo proekta.

# POLIMORPHIZM DOSTIGAETSYA 2 METODAMI:
# 1. PEREGRUZKA(OVERLOADING)

class Base:
    def __init__(self, a):
        self.__a = a

    def print_a(self, square = False, multiplier = None):
        if square and not multiplier:
            print(self.__a ** 2)
        elif not square and multiplier:
            print(self.__a * multiplier)
        elif square and multiplier:
            print((self.__a ** 2) * multiplier)
        else:
            print(self.__a)


base = Base(4)
base.print_a()
base.print_a(square=True)
base.print_a(square=True, multiplier=2)
base.print_a(multiplier=2)

print("-----------------")


class Car:
    def __init__(self, name):
        self._speed_name_map = {
            "BMW": 250,
            "Mercedes": 350
        }
        self._max_speed = self._define_max_speed(name)

    def _define_max_speed(self, name):
        return self._speed_name_map.get(name, 0)

    def distance_on_max_speed(self, distance):
        if self._max_speed == 0:
            print(
                "Speed = 0, select valid car brand: {}".format(
                    list(self._speed_name_map.keys())
                )
            )
            return 0
        return distance / self._max_speed


car1 = Car("BMW")
car2 = Car("Mercedes")
car3 = Car("ABC")
print(car1.distance_on_max_speed(100))
print(car2.distance_on_max_speed(100))
print(car3.distance_on_max_speed(100))

print("-----------------")


class Animal2:
    def __init__(self, name):
        self._name = name

    def voice(self):
        if self._name == "cat":
            print("Meow")
        elif self._name == "dog":
            print("Bark")
        else:
            print("...")


a1 = Animal2("cat")
a1.voice()
a2 = Animal2("dog")
a2.voice()
a3 = Animal2("dinosaur")
a3.voice()

print("-----------------")

# 2. PEREOPREDELENIE


class Multiplier:
    def __init__(self, a):
        self._a = a

    def print_a(self, x):
        print(self._a * x)


m = Multiplier(5)
m.print_a(2)


class Exponent(Multiplier):
    def print_a(self, x):
        print(self._a ** x)


e = Exponent(4)
e.print_a(2)

print("-----------------")


class Animal:
    def __init__(self, name):
        self._name = name

    def voice(self):
        pass


class Cat(Animal):
    def voice(self):
        print("Meow")


class Dog(Animal):
    def voice(self):
        print("Bark")


animal = Animal("?")
animal.voice()

cat = Cat("Sarah")
cat.voice()
dog = Dog("Rex")
dog.voice()

print("-----------------")

# Kak na praktike on primenim

# Plohoy primer polimorphizma na praktike:


class Messenger:
    def __init__(self, connection):
        self._connection = connection

    def send_message(self, text, option=None):
        self._connection.send(text)


# Nakruchivat mnogo vsego na prostie metodi plohaya praktika
class ExtendedMessenger(Messenger):
    def send_message(self, text, option=None):
        if option == "message":
            self._connection.send(text)
        elif option == "image":
            self._connection.send(text)
        elif option == "math":
            print("2+2=4")
        else:
            print("...")


print("-----------------")

# Reshenie zadach
# ZADACHI:

# ZADACHA 1:
# Napisat class Parallelogram, kotoriy imeet 2 argumenta width i length(shirina i dlina) i metod
# get_area, kotoriy vozvrashaet ploshd parallelogramma s takimi storonami. Unasledovat ot nego
# class Square, pereopredelit metod get_area kak proizvedenie shirini na shiriny (ili dlini na
# dliny).


class Parallelogram:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def get_area(self):
        return self._width * self._length


class Square(Parallelogram):
    def get_area(self):
        return self._width * self._width


print("-----------------")

# ZADACHA 2:
# Napisat funkciyu, kotoraya prinimaet 2 parametra data i new_value. Esli data eto spisok ili
# mnozhestvo, to dobavit v nego element new_value, esli stroka, to skonkatenirovat (za isklyucheniem,
# esli new_value ne spisok, inache vernut ne izmenennyuy data), a esli eto chislo, logicheskoe
# znachenie ili slovar, to vernut ne izmenennuyu data.


def function(data, new_value):
    if isinstance(data, list):
        data.append(new_value)
    elif isinstance(data, set):
        data.add(new_value)
    elif isinstance(data, str):
        if isinstance(new_value, str):
            data += new_value
    return data


print(function([1, 2, 3], 4))
print(function({1, 2, 3}, 4))
print(function({1, 5, 3}, 4))
print(function("{1, 2, 3}", 4))
print(function({1, 2, 3}, "4"))
print(function("{1, 2, 3}", "4"))

print("-----------------")