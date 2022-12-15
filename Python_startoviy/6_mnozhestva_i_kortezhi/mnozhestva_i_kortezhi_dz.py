# Est dva mnozhestva
# Zadanie 1: vivesti v konsol elemeti a kotorih net v b

a = {3, 5, 11, 7, 4, -3}
b = {11, 5, 8, 1, 10, 7}
print(a)
print(b)
print(a.difference(b))

print("------------------------------")

# Zadanie 2: vivesti v konsol obshie elemety

print(a.intersection(b))

print("------------------------------")

# Zadanie 3: vivesti v konsol obyedinenie mnozhestv a i b

print(a.union(b))

print("------------------------------")

# Zadanie 4: est stroka  c = "a14b6fh", kak uznat, chto vse simvoly unikalny,
# ispolzuya mnozhestva i spiski.

a = "a14b6fh"
# d = "a14b6hh"
b = list(a)
c = set(a)
print("unique character") if len(b) == len(c) else print("not unique character")