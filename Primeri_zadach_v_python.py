# ZADACHA 1:
# POLUCHENIE CHISLA FAKTORIALA PRI POMOSHI REKURSIYI


def fact(x):
    if x == 1:
        return 1
    return fact(x - 1) * x


print(fact(8))


# 1 * 1 1
# 2 * 3 6
# 6 * 4 24
# 24 * 5 120
# 120 * 6 720
# 720 * 7 5040
# 5040 * 8 40320
# 40320 * 9 362880
# 362880 * 10 3628800

print("-------------------------------------")


# ZADACHA 2:
# POLUCHENIE CHISLA FIBONACHI OT VVEDENNOGO CHISLA PRI POMOSHI REKURSIYI


def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(7))

print("-------------------------------------")


# ZADACHA 3:
# PROVERKA STROKI NA POLYNDROM PRI POMOSHI REKURSIYI


def palindrom(s):
    if len(s) <= 1:  # proverka dlinni stroki
        return True
    if s[0] != s[-1]:  # proverka na sravnenie 1 i poslednego simvola na ravenstvo
        return False
    return palindrom(s[1:-1])  # proverka vsey stroki pri pomoshi sreza s 1 po posledniy simvol


print(palindrom("к"))
print(palindrom("пп"))
print(palindrom("ка"))
print(palindrom("калук"))

print("-------------------------------------")


# ZADACHA 4:
# VVODITSYA STROKA NE NYLEVOY DLINI. IZVESTNO TAKZHE, CHTO DLINA NE PREVISHAET 1000 ZNAKOV.
# VIVESTI STROK, KOTORAYA POLUCHITSYA POSLE DOBAVLENIYA SKOBOK.
# PRIMER:
# STROKA = lItBeoFLcSGBOFQxMHoIUDDWcqcVgkcRoAeocXO
# RESULTAT = l(I(t(B(e(o(F(L(c(S(G(B(O(F(Q(x(M(H(o(I)U)D)D)W)c)q)c)V)g)k)c)R)o)A)e)o)c))X)O


def rec(sw):
    if len(sw) == 1 or len(sw) == 2:
        return sw
    return sw[0] + '(' + rec(sw[1:-1]) + ')' + sw[-1]


# sw = input()
# print(rec(sw))

print("-------------------------------------")


# ZADACHA 5:
# FUNKCIYA V KOTOROY CHISLO "X" VOZVODITSYA V STEPEN "N" PRI POMOSHI REKURSIYI


def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1/power(x, -n)  # vozvedenie v otricatelnuyu stepen
    if n % 2 == 0:
        return power(x, n // 2) * power(x, n // 2)
    else:
        return power(x, n - 1) * x


# x = int(input())
# n = int(input())
# print(power(x, n))

print("-------------------------------------")


# ZADACHA 6:
# EST SPISOK NADO OPREDELIT NA KAKOM UROVNE NAHODITSYA KAZHDIY IZ VLOZHENNIH SPISKOV

a = [1, [3, [4, [3, 4]], [2, 3, [4]]], 2, [2, 3, 4, [3, 4, [2, 3], 5]]]


def rec_num(spicok, level=1):
    pass
    print(*spicok, 'level=', level)  # * - chtobi vse elementy raspakovalis i vivelis cherez probel bez kvadrathih skobok
    for i in spicok:
        if type(i) == list:
            rec_num(i, level+1)


rec_num(a)

print("-------------------------------------")


# ZADACHA 7:
# OBHOD FAILOV V PAPKE PRI POMOSHI REKURSIYI


import os  # import module os

path = 'C:\\Users\\p6334\\OneDrive\\Desktop\\test_python'  # dobavlenie \ dlya korektnogo otobrazheniya puti

print(os.listdir(path))  # perechen soderzhimogo puti


def obxodFile(path, level=1):
    print('level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('Спускаемся', path + '\\' + i)
            obxodFile(path + '\\' + i, level + 1)
            print('Вовращаемся в', path)


obxodFile(path)

# for i in os.listdir(path):  # perebor soderzhimogo puti
#       print(i, type(i), path + '\\' + i, os.path.isdir(path + '\\' + i))
# isdir - proverka na papky
# isfile - proverka na fayl
# proverka soderzhimogo na tip i proverka chto yavlyaetsya papkoy a chto faylom
