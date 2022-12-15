# Zadacha 1:
# Napisat class kotoriy opisivaet polzovatelya(class User), sdelat emy privatniy attribut age,
# kotoriy peredayotsya v konstruktor, publichniy attribut name, kotoriy tak zhe peredayotsya
# v konstruktor.

# Zadacha 2:
# Napisat getter i setter dlya attributa age.

# Zadacha 3:
# Dobavit v setter proverky na validniy vozrast (ne otricatelnoe, celoe chislo).


class User:
    def __init__(self, age, name):
        self.__age = age
        self.name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
        if value >= 0 and value == int(value):
            print("{} is old {}".format(
                self.name,
                self.__age
            ))
        else:
            print("Ne celoe ili otricatelnoe chislo")


user = User(age=25, name="Alex")
print(user.age)
user.age = 13
