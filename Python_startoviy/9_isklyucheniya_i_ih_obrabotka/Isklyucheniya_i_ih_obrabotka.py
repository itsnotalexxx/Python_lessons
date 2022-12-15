# Ponyatie isklyucheniya
# Iscklyucheniya - eto mehanizm dlya obrabotki zavedomo izvestnih oshibok i drugih
# vozmozhnix problem, vo vremya vipolneniya programmi.
# Kak primer - eto delenie na 0. Dalee razberemsya kak obrabativat ety oshibky.

a = 10
b = 0
# c = a / b
# print(c)

# Dlya chego nuzhni isklyucheniya:

# 1) Vozmozhnost vivesti chitaemiy tekst pri vozniknivenii oshibke.
# 2) Programma ne budet padat.
# 3) Propisivaya isklyucheniya, vi luchshe produmivaete logiky vashego koda.

print("-------------------")

# Kak obrabativat isklyucheniya:

# Dlya obrabotki isklyucheniy ispolzyetsya blok try - except.

# try:
#   some sode
# except:
#   some action

d = 10
f = 0

try:
    g = d / f
except:
    g = 0
    print("division on zero")
print(g)

print("-------------------")


# Vidi isklyucheniy:

# Dlya togo chtobi obrabotka oshibok bila bolee tochechnoy, mozhno ukazivt opredelenniy tip
# oshibki, kotoriy vi ozhidaete.

# Iznachalno otlavlivayutsya oshibki BaseException, pod kotorie popadayut lyubie oshibki.
# try:
#   ...
# except BaseException:
#   ...

# Chasto vstrechayushiesya vidi isklyucheniy:

# BaseException - otlavlivaet vse oshibki.
# NameError - ne naydeno peremennuyu s takim imenem.
# TypeError - neverniy tip obyekta, k kotorome primenyaetsya operaciya.
# ValueError - oshibka, svyazannaya so znacheniem argumenta.
# AssertionError - virazhenie v funkciyi assert lozhno.
# ImportError - ne udalos importirovat modulya ili ego atributa.

def x():
    a = 10


try:
    print(abc)
except NameError as error:
    print(error)

print("-------------------")

try:
    print(int('abc'))
except ValueError as error:
    print(error)

print("-------------------")

# assert - proveryaet ravenstvo, k primery:
# assert 2 == 2

assert 2 == 2
# assert 2 == 3 # Oshibka

try:
    assert 2 == 3
except AssertionError as error:
    print(error)

print("-------------------")

z = None
try:
    for elem in z:
        print(elem)
except TypeError as error:
    print(error)

print("-------------------")

# Primeri isklyucheniy i ih obrabotki:

# 1. Realizovat funkciyu, kotoraya budet prinimat na vhod nomer mesyaca, vernut ego nazvanie
# i realizovat v nem neskolko obrabotok isklyucheniy.

def get_month(number):
    months = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    try:
        return months[number]
    except KeyError as key_error:
        print(key_error, ", use only numbers from 1 to 12")
    except TypeError as type_error:
        print(type_error, ", use only numbers from 1 to 12")


month_name = get_month([1, 2, 3])
print(month_name)
print("-------------------")

# 2. Nuzhno proverit, vse chisla v posledovatelnosti unikalni i realizovat neskolko obrabotok
# isklyucheniy.

def check(sequence):
    if len(set(sequence)) == len(sequence):
        return True
    return False

def check_sequence_unique(array):
    try:
        return(check(array))
    except TypeError as type_error:
        print(type_error, 'use only strings, lists or sets')


s = [1, 2, 3, 4]
y = 'abcd'
u = check_sequence_unique(y)
print(u)


print([1, 2, 3, 4, 5][1:3])


a = 10
b = 5

if a % 4 - a // 4 > 0:
    print(1)
else:
    print(a % b)


d = {"a": 10, "b": 5, "c": 7}
s = ""

for x in d:
    s += x

print(s)


x = 1

b = "hello"

if len(b) == len(b * x):
    print(1)

if len(b) * 2 < len(b):
    print(2)

elif x > 0:
    print(3)

else:
    print(4)

if x * x > x ** x:
    print(5)


fd = {1, 2, 3}

fd.add(3)
print(fd)

for i in range(0, 11, 2): print(i)