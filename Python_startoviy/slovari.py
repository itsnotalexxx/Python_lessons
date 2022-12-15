my_dict = {'key': 'value', 10: True, 0.2: 'Hello'}
# V slovaryah obrashaemsya tolka k kluchy, a ne k znacheniyu
print(my_dict)
print(my_dict[0.2])
print(my_dict.get(10))
print("------------------------")

# clear() - ochishayet slovar

d = {1: 10, 2: 20}
print(d)
d.clear()
print(d)
print("------------------------")

# items() - vozvrashaet pary klyuch - zhachenie v formate spisok kortezhey

c = {1: 10, 2: 20}
print(c.items())
print("------------------------")

# pop(key) - udalyaet i vozvrashaet sootvetstvuyushee emy zhachenie

e = {"hello": "world", "hi": "world"}
print(e.pop('hello'))
print(e)
print("------------------------")

# popitem() - udalyaet posledneye zhachenie i vozvrashayet ego v formate klyuch - znachenie

c = {1: "fd", 2: "dfd"}
print(c.popitem())
print(c)
print("------------------------")

# update({'key': 'value'}) - dobavlyaet novoe klyuch - znachenie

b = {1: 3, 2: 4, 5: 2}
b1 = {55: 6, 45: 3}
print(b)
b.update({6: 30})
print(b)
print(b1)
b1.update(b)
print(b1)
print("------------------------")

# values() - vozvrashaet vse znacheniya v slovare

b3 = {1: 3, 2: 4, 5: 2}
print(b3)
print(b3.values())
print("------------------------")

# Chto mozhna delat pri pomoshi slovarya:

# 1. Poschitat skolko raz element povtoryaetssya v spiske

my_list = [1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 7, 7, 7, 7]
value_to_count = 5
count_dict = {value_to_count: 0}
for element in my_list:
    if element == value_to_count:
        count_dict[value_to_count] += 1
print(count_dict)

# 1.1 Skolko raz povtoryautsya vse elementi

my_list2 = [1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 7, 7, 7, 7]
count_dict2 = {}
for elem in my_list2:
    if elem in count_dict2:
        count_dict2[elem] += 1
    else:
        count_dict2[elem] = 1

print(count_dict2)

for key, value in count_dict2.items():
    print("Key:", key, "count", value)

print("------------------------")

# 2. Proytis po slovaryu i vivesti vse znacheniya u kotorix est chetkiy klyuch
# 3. Udalit vse klyuchi, zhacheniya kotorih nachinayutsya s bukvi a

