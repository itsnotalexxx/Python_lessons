# Incapsulyaciya
# Incapsulyaciya - eto princip, pri kotorom polzovatel ispolzyet tolko publichnuyu ili
# "interfeisnuyu" chast classa i ne vnikaet v ego vnytrenuyuy realizaciyu.

# Takim obrazom programmist ckrivaet opredelennie dannie, metodi, atributi ot posledyuyshih
# polzovateley.

# Specialnie metodi - getteri i setteri.

# Incapsulyaciya v Python:

# Urovni dostupa v incapsulyaciyi:
# 1. _ - nizhnie podcherkivanie delaet dannie protected
# 2. __ - delaet dannie privat


class Test:
    def __init__(self, test_value, test_value_2):
        self._public_attr = test_value
        self.__private_attr = test_value_2

    def get_private_attr(self):
        return self.__private_attr

    def __private_function(self):
        print("I am private")

    def call_private(self):
        self.__private_function()


test = Test(test_value=10, test_value_2=15)
print(test._public_attr)
print(test.get_private_attr())
test.call_private()

print("--------------------------")


class User:
    def __init__(self, name):
        self.__name = name

    @property  # getter
    def name(self):
        return self.__name

    @name.setter  # setter
    def name(self, value):
        self.__name = value


user = User(name="Alex")
print(user.name)
user.name = "Bob"
print(user.name)

print("--------------------------")


class Worker:
    RIGHTS = "Equal"
    SALARY_MAP = {
        "A": 100,
        "B": 200,
        "C": 500
    }

    def __init__(self, working_class):
        self.__salary = self.__get_salary(working_class)

    @staticmethod
    def __get_salary(working_class):
        return Worker.SALARY_MAP.get(working_class, 0)

    @property
    def salary(self):
        return self.__salary


w1 = Worker("A")
print(w1.salary)
w2 = Worker("B")
print(w2.salary)
w3 = Worker("X")
print(w3.salary)


print("--------------------------")


class User2:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("Property was called")
        return self.__name


u2 = User2(name="Mike")
print(u2.name)

print("--------------------------")

# PRAKTIKA
# ZADACHI:

# ZADACHA 1:
# Napisat class TextProcessor dlya obrabotki tekstovih dannih. Class dolzhen imet publichniy
# metod get_clean_string, kotoriy udalit vse znaki prepinaniya iz stroki, kotoruyu v nego
# peredayut argumentom i privatniy metod is_punktuation, kotoriy neposredstvenno proveryaet simvol
# na ravenstvo so znakami punktuaciyi i vozvrashaet True/False, kotorie v svoyu ochered
# yavlyayutsya privatnim ili zashishenim atributom classa.


class TextProcessor:
    def __init__(self):
        self._punktuation = ".,!?;:"

    def __is_punktuation(self,char):
        return char in self._punktuation

    def get_clean_string(self, text):
        clean_text = ""
        for char in text:
            if self.__is_punktuation(char):
                continue
            clean_text += char
        return clean_text


p = TextProcessor()
print(p.get_clean_string("Hello! World?"))

print("--------------------------")

# ZADACHA 2:
# Napisat class TextLoader, kotoriy imeet privatnim attributom text_processor obyekta classa,
# chto bil sozdan v zadache 1. Noviy class budet imet privatniy atribut clean_string i publichniy
# metod set_clean_text, kotoriy budet vizivat metod classa TextProcessor cherez svoy attribut
# text_processor i zapisivat znachenie v clean_string. Sam zhe attribut clean_string budet imet
# property s dopolnitilnim vivodom v konsol togo, chto vivoditsya uzhe ochishenaya stroka.


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_string(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print("Clean string is: {}".format(
            self.__clean_string
        ))
        return self.__clean_string


print("--------------------------")

# ZADACHA 3:
# Napisat class DataInterface, kotoriy budet imet svoim zashishenim attributom obyekt classa
# TextLoader i publichniy metod process_texts, kotoriy budet prinimat spisok strok, v cikle
# obrabotaet kazhduyu i vivedet ee znachenie v konsol.


class DataInterface:
    def __init__(self):
        self.__text_loader = TextLoader()

    def process_texts(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_string(text)
            clean = self.__text_loader.clean_string
            clean_texts.append(clean)
        return clean_texts


di = DataInterface()
t = ["Hello, I am John", "Hey, what is the weather today?"]
ct = di.process_texts(t)

print("--------------------------")