# Ponyatie mnozhestv

# Mnozhestva - eto struktura dannih, ne soderzhashshaya povtoryaushihsya elementov.
# Mnozhestva ne podderzhivayut indeksaziyu, poetomy dostup k elementam vozmozhen pereborom.
# Sintaksis mnozhestv {1, 4, 2, 3}
# Mnozhestva yavlyayutsya avtomaticheski sortiryemie po poryadky
# set - eto pustoe mnozhestvo

a = {1, 2, 3, 4, 4, 4, 4, 4, 4}
print(a) # {1, 2, 3, 4}

print("------------------------------")

# Metodi mnozhestv

# clear() - ochishayet mnozhestvo

b = {1, 2, 3, 4}
print(b) # {1, 2, 3, 4}
b.clear()
print(b) # set{}

print("------------------------------")

# pop() - udalyaet perviy element mnozhestva

c = {1, 2, 3, 4}
print(c) # {1, 2, 3, 4}
c.pop()
print(c) # {2, 3, 4}
c.pop()
print(c) # {3, 4}

print("------------------------------")

# discard(elem) - udalyaet element iz mnozhestva

d = {1, 2, 3}
print(d) # {1, 2, 3}
d.discard(3)
print(d) # {1, 2}

print("------------------------------")

# remove(elem) - udalyaet element iz mnozhestva. Esli takogo elementa net, vidaet oshibky

e = {1, 2, 3}
print(e) # {1, 2, 3}
e.remove(2)
print(e) # {1, 3}

print("------------------------------")

# add(elem) - dobavlyaet element vo mnozhestvo

f = {1, 2, 4, 6, 3, 5}
print(f)
f.add(7)
print(f)

print("------------------------------")

# union(another_set) - obyedinyaet mnozhestva

g = {1, 2, 3}
h = {4, 5, 6}
print(g)
print(h)
g.union(h)
print(g)
print(g.union(h))

print("------------------------------")

# intersection(another_set) - nahodit peresechenie dvuh mnozhestv

j = {1, 2, 3}
k = {4, 5, 6}
m = {2, 3}
print(j)
print(k)
print(m)
print(j.intersection(k))
print(j.intersection(m))

print("------------------------------")

# difference(another_set) - raznica mnozhestv

n = {1, 2, 3, 4}
x = {3, 4, 5}
print(n)
print(x)
print(n.difference(x))
print(x.difference(n))

print("------------------------------")

# elem in set_name - nahoditsya li element v mnozhestve

y = {1, 2, 3, 4}
print(y)
print(1 in y)
print(5 in y)

print("------------------------------")

z = [1, 2, 3, 4, 5, 6] # tozhe samoe rabotaet i v spiskah
print(z)
print(5 in z)
print(10 in z)

print("------------------------------")

# Ponyatie kortezhey

# Kortezh(tuple) - eto neizmenyaemiy spisok(nelzya ne dobavit/ne udalyt. Kak konstanta.
# No on mozhet hranit dublikati kak i spisok.
# sintaksis kortezhey:
# (1, 2, 3)
# (1,)

a1 = (1, 2, 3, 4)

print("------------------------------")

# Metodi kortezhey

# Mozhno ispolzovat vse metodi kotorie ne izmenyayut ego.
# Chasto ispolzyyut ih chto bi menyat elementi mestami, k primery:
# a, b = b, a

b1 = (1, 2)
x1, y1 = b1
print(b1)
print(x1, y1)
x1, y1 = y1, x1
print(x1, y1)

print("------------------------------")

# Takzhe, pri prohozhdenii po spisky kortezhey, cikl for mozhet prinimat
# stolko znacheniy, skolko elementov v kortezhe(tuple).
# sintaksis:
# for elem1, elem2 in [(1, 2), (2, 4)]

a3 = [(1, 2), (3, 4)]
print(a3)
for first, second in a3:
    print(first, second)

print("------------------------------")

b2 = [(1, 2, 3), (3, 4, 5)]
print(b2)
for first, second, third in b2:
    print(first, second, third)

print("------------------------------")