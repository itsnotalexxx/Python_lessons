# O chem etot kurs.

# 1. OOP: nasledovanie, inkapsulyaciya, polimorphizm i abstrakciya.

# Koncepciya OOP sostoit iz 4 factorov:
# - NASLEDOVANIE
# - ABSTRAKCIYA
# - INKAPSULYACIYA
# - POLIMORPHIZM

# Chto takoe OOP.

# OOP - metodologiya programirovaniya, osnovannaya na predstavlenii programmi v vide sovokupnosti
# obyektov, kazhdiy iz kotorih yavlyaetsya ekzemplyarom opredelyonogo klassa, a klassi obrazyuyt
# ierarhiyu nasledovaniya.

# Chto takoe NASLEDOVANIE:
# NASLEDOVANIE - eto koncepciya obyektno-orientirovannogo programirovaniya, soglasno
# kotoroy abstraktniy tip dannih mozhet nasledovat dannie i funkcionalnost nekotorogo
# syshestvyeshego tipa, sposobstvuya povtornomy ispolzovaniyu komponentov programmnogo obespecheniya.

class Human: # nazvanie klassa pishetsya s bolshoy bukvi
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name

    def get_age_and_name(self):
        return self.age, self.get_name() # or self.name


human_1 = Human(age=25, name="John", gender="male")
print(human_1.age)
print(human_1.get_name())
print(human_1.get_age_and_name())

print("------------------------")

# Bivayut 2 vida nasledovaniya:

# 1. Edinoe:
# Eto kogda odin roditel.

class Humman:
    def __init__(self, age):
        self.age = age

    def say_hello(self):
        print("Hello, I am {}".format(self.age))


humman = Humman(age=35)
humman.say_hello()


class HumanExtended(Humman):
    def __init__(self, age, name):
        super().__init__(age) # super - vizov roditelskog klassa.
        self.name = name

    def say_hello(self):
        print("Hello, I am {} and I am {}".format(
            self.name, self.age
        ))


human2 = HumanExtended(age=56, name="John")
human2.say_hello()

print("------------------------")

# 2. Mnozhestvennoe
# Kogda bolshe odnogo roditelya.


class A:
    def __init__(self):
        self.a = 10


class B:
    def __init__(self):
        self.b = 5


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)


c = C()
print(c.a)
print(c.b)

print("------------------------")

# Primeri ispolzovaniya OOP i nasledovaniya na praktike.

# Zadachi:

# 1. Napisat klass avtomobilya s atribytami marki, cveta i obiema dvigatelya i metodami: ehat
# vpered i ehat nazad.


class Car:
    def __init__(self, brand, color, volume):
        self.brand = brand
        self.color = color
        self.volume = volume

    @staticmethod
    def drive_forward():
        print("Drive forward")

    @staticmethod
    def drive_backward():
        print("Drive backward")


car = Car(brand="Audi", color="black", volume=2.4)
car.drive_forward()
car.drive_backward()
Car.drive_forward()
Car.drive_backward()

print("------------------------")

# 2. Napisat klass avtomobilya unasledovannogo ot pervogo klassa v pynkte 1. Dobavit
# metodi povorota nalevo i napravo.


class Car2(Car):
    @staticmethod
    def turn_left():
        print("Turn left!")

    @staticmethod
    def turn_right():
        print("Turn right")


car = Car2("Audi", "white", 3.5)
car.turn_left()
car.drive_backward()
car.turn_right()
car.drive_forward()

print("------------------------")

# 3. Napisat klass samoleta, imeyushego metod vzletat i atribut model samoleta.


class Airplane:
    def __init__(self, model):
        self.airplane_model = model

    @staticmethod
    def up():
        print("Going up!")

    @staticmethod
    def land():
        print("Landing")


print("------------------------")

# 4. Napisat klass, unasledovanniy ot mashini (2 zadacha) i ot samoleta (3 zadacha).
# Posmotret chto budet.


class FlyingCar(Car2, Airplane):
    def __init__(self, brand, color, volume, model):
        Car2.__init__(self, brand, color, volume)
        Airplane.__init__(self, model)


fc = FlyingCar(brand="Tesla", color="Black", volume=10, model="F")
fc.up()
fc.drive_forward()
fc.turn_left()
fc.drive_backward()
fc.land()


print("------------------------")

# P.S. Vse metodi - eto prosto komanda pechati, naprimer print("Drive forward") i t.d.

# Analogichnoe reshenie etih zadach:

class Ccar:
    def __init__(self, brand, color, vol):
        self.brand = brand
        self.color = color
        self.vol = vol

    @staticmethod
    def ddrive_forward():
        print("Drive forward")

    @staticmethod
    def ddrive_backward():
        print("Drive backward")


class Ccar2(Ccar):
    def __init__(self, brand, color, vol):
        super().__init__(brand, color, vol)

    @staticmethod
    def tturn_left():
        print("Turn left!")

    @staticmethod
    def tturn_right():
        print("Turn right!")


class Aairplane:
    def __init__(self, model):
        self.model = model

    @staticmethod
    def fly():
        print("Start the flight")


class FflyingCar(Ccar2, Aairplane):
    def __init__(self, brand, color, vol, model):
        Ccar2.__init__(self, brand, color, vol)
        Aairplane.__init__(self, model)


fflying_car = FflyingCar(
    brand="Tesla",
    color="Black",
    vol=4.5,
    model="F"
)

fflying_car.fly()
