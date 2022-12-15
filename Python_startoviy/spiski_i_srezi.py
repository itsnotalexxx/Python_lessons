# spiski
my_list = list("abcd") # list sozdaet spisok
print(my_list)

my_list2 = ['a', 35, 'c', False] # [] - spisok
print(my_list2)

print("------------")

# srezi

my_list3 = [1, 2, 3, 4, 5]
print(my_list3[3])
print(my_list3[0:3])
print(my_list3[0:3:2]) #list[start:end:step]

print("------------")

# metodi spiskov

# append() - dobavlenie elementa v konec spiska
# clear() - udalit vse elementi spiska

a = [1, 2, 3]
print(a)
a.append("hello")
print(a)
a.append(5)
print(a)
a.clear()
print(a)

print("------------")

# extend() - rasshiryaet spisok peredanoi posledovatelnosti
# index() - vozvrashaet index ukazanogo elementa, esli takix neskolko - vernet perviy naidenuy

b = [1, 2, 3]
c = [4, 5, 6]
print(b)
print(c)
b.extend(c)
print(b)
print(b.index(4))
print(b+c)
print(b)
b = b + c
print(b)
b += c
print(b)

print("------------")

# pop() - udalyaet element ukazanogo indexa i vozvrashaet ego
# reverse() - zerkalnoe otobrazhenie spiska

d = [1, 2, 3, 4]
removed_element = d.pop(0)
print(d)
print(removed_element)
d.reverse()
print(d)
d.reverse()
print(d)

print("------------")

# sort - sortiryet spisok. Esli ukazani v parametrah reverse=True, togda sortirovka budet reverse

e = [5, 2, 1, 3, 6, 4]
print(e)
e.sort()
print(e)
e.sort(reverse=True)
print(e)

print("------------")

# Obhod spiskov
# spiski mozhno obhodit pri pomoshi ciklov

flist = [4, 3, 2, 1]
for element in flist:
    print(element)

print("_________________")

# Zadazhi so spiskami
# Zadacha 1: Nayti i udalit chetnie elemety spiska

glist = [1, 2, 3, 4, 5, 6]
for element in glist:
    if element % 2 == 0:
        print(element)

print("_________________")

# Zadacha 1: vivesti chetnie elementy spiska v drugoi spisok

glist = [1, 2, 3, 4, 5, 6]
hlist = []

for element in glist:
    if element % 2 == 0:
        hlist.append(element)
print(hlist)

print("_________________")

# Zadacha 2: vozvesti vse elementy spiska v kvadrat

jlist = [2, 4, 6, 8]
klist = []

for elem in jlist:
    klist.append(elem**2)
print(klist)

print("_________________")

# Zadacha 3: nayti maksimalniy element spiska

x = [3, 2, 1, 7, 0, -3, 25, -78, 45, 100, -1, 10]
max_element = x[0]
for element in x:
    if element > max_element:
        max_element = element
print(max_element)

print("_________________")

# Zadacha 4: nayti minimalniy element spiska

x = [3, 2, 1, 7, 0, -3, 25, -78, 45, 100, -1, 10]
min_element = x[0]
for element in x:
    if element < min_element:
        min_element = element
print(min_element)

print("_________________")