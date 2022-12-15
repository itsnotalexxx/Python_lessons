# Oblast vidimosti funkciyi

# Oblast vidimosti - eto oblast, v kotoroi interpretatory dostupni vashi peremennie,
# funkciyi i prochee. Oblast vidimosti bivaet lokalnaya i globalnaya.

# Peremennie, kotorie obyavleni vne funkciyi, nazivayutsya globalnimi peremennimi v python.
# Eti peremennie imeyut bolshuyu oblast vidimosti i dostupni vsem funkciyam, kotorie opredeleni
# posle oblyavleniya globalnoy peremennoy.

# Kogda peremennaya obyavlyaetsya vnytri funkciyi, to eto lokalnaya peremennaya. Oblast deystviya localnoy
# peremennoy ogranichena funkciey, v kotoroy ona sozdayotsya. Eto oznachaet, chto ona
# dostupna v funkciyi, gde ona obyavlena, no ne vne etoy funkciyi.

# Globalnaya peremennaya

x = 1
print(x)


def print_x():
    print(x)


print_x()

# Localnaya peremennaya


def print_y():
    y = 19
    print(y)


print_y()


def print_z():
    z = 10
    return z


z_from_local = print_z()
print(z_from_local)

print("-------------------")

# Vlozhenie funkciyi


def main():
    x = 10
    def internal():
        return 1

    internal_result = internal()
    return x + internal_result

m = main()
print(m)

print("-------------------")

# Standartnie funkciyi v python

# V python sushestvyet mnozhestvo vstroenih funkciy, kotorie mozhno i nuzhno ispolzovat dlya
# uprosheniya vashego koda.

# print - funkciyi dlya vivoda soobsheniy v konsol.
# len - funkciya, kotoraya vozvrashaet dliny obekta.
# str - preobrazovanie v stroky.
# int - preobrazovanie v celoe chislo.
# float - preobrazovanie v ne celoe chislo.
# list - preobrazovanie v spisok.
# dict - preobrazovanie v slovar.
# set - preobrazovanie v mnozhestvo.
# tuple - preobrazovanie v kortezh.
# bool - preobrazovanie v True/False.
# sum - vozvrashaet summu nabora chisel.
# min - vozvrashaet minimum iz nabora chisel.
# max - vozvrashaet maksimum iz nabora chisel.

print('a', 1, 2, "b")
print([1, 2, 3])
print(['1', [2], [3, [4]]])

print("-------------------")

a = [1, 2, 3, 4]
print(len(a))

print("-------------------")

d = 1
print(d)
print(str(d))
d_str = str(d)
print(type(d_str))

print("-------------------")

e = 2
print(e)
print(int(e))
e_int = int(e)
print(type(e_int))

print("-------------------")

f = 3
print(f)
print(float(f))
f_float = float(f)
print(type(f_float))

print("-------------------")

g = []
print(g)
print(bool(g))
g1 = {}
print(g1)
print(bool(g1))
g2 = ()
print(g2)
print(bool(g2))
g3 = None
print(g3)
print(bool(g3))
g4 = -1
print(g4)
print(bool(g4))
g5 = 10
print(g5)
print(bool(g5))
g6 = [1, 2, 3]
print(g6)
print(bool(g6))

print("-------------------")

h = [1, 2, 3, 4, 5]
print(h)
print(sum(h))
print(sum(h)/len(h)) #uznaem srednyu summu

print("-------------------")

j = [1, 2, 3, 4, 5]
print(j)
print(min(j))
print(max(j))

print("-------------------")

# Anonimnie funkciyi

# Anonimnie funkciyi - ispolzyuytsya v sluchae, esli nam ih nuzhno kuda-to peredat i bolshe
# mi ih ne budem ispolzovat povtorno. Takaya zapis budet kompaktnee. U takoy funkciyi ne
# budet imeni.
# sintaksis:
# lambda x: x
# Gde perviy x - eto parametr, kotoriy peredayotsya v funkciyu, a vtoroy - to, chto vozvrashaetsya.
# V sravnenie s obichnoy funkciey:
# def some_name(x):
#   return x

k = [1, 2, 3, 4, 5]

def make_smth(function):
    for element in k:
        print(function(element))


make_smth(lambda l: l + 10)
make_smth(lambda n: n - 4)

print("-------------------")

# Rekursiya
# Rekursiya - eto kogda funkciya vizivaet sama sebya. V rekursiyi obyazatelno dolzhno but
# konechnaya glubina dlya togo, chtobi ne bilo zaciklivaniya.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))

print("-------------------")

# Primeri raboti s funkciyavi

# 1. Napishite funkciyu, gde dano naturalnoe chislo n. Vivedite vse chisle ot 1 do n.

def numbers(n):
    for number in range(1, n + 1):
        print(number)


numbers(5)

print("-------------------")

# 2. Napishite funkciyu dlya proscheta ploshadi pryamougolnika, v parametrah peredautsya
# visota i dlinna.

def rectangle(height, length):
    return height * length


heig = 10
leng = 45
area1 = rectangle(heig, leng)
print(area1)