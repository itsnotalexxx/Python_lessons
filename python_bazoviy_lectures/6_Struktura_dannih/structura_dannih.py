# PLAN UROKA
# Primeri kombinaciyi struktur dannih i rabota s nimi
# Slozhnie obyekti

user = {
    "name": "JohnDoe",
    "info": {
        "basic": {
            "age": 25,
            "salary": 5000
        },
        "additional": {
            "study": "mathematics",
            "family": "married"
        },
        "special": {
            "projects": [
                {"name": "quantum_computer", "stage": "in_progress"},
                {"name": "laser_gun", "stage": "in_production"}
            ]
        }
    }
}


def get_data(data_dict, keys):
    data = data_dict
    for key in keys:
        data = data[key]
    return data


print(get_data(user, ["info", "special", "projects", 0, "name"]))
print("-----------------------")


# tazhe funkciya tolko pri pomoshi Rekursiyi

def get_data_rec(data_dict, keys, index=0):
    if index < len(keys):
        return get_data_rec(data_dict[keys[index]], keys, index + 1)
    return data_dict


print(get_data_rec(user, ["info", "special", "projects", 0, "name"]))
print("=======================")


# Comprehensions v Python
# List comprehension

chars = []
for char in "abcde":
    chars.append(char)
print(chars)
print("-----------------------")


chars2 = [char for char in "abcde"]
print(chars2)
print("-----------------------")


names = ['make', 'john', 'sally']
names = [name.capitalize() for name in names]
print(names)
print("-----------------------")

numbers = [1, 2, 3, 4, 5, 6]
# even_nums = [num for num in [1, 2, 3, 4, 5, 6]] mozhna obyavit obyekt pryamo v cikle
even_nums = [num for num in numbers if num % 2 == 0]  # dobavlenie IF posle iteracii, vivodim tolko chetnie
print(even_nums)
print("=======================")


# Set comprehension

unique_values = {value ** 2 for value in [1, 3, 5, 5, 2, 2, 1, 7]}  # ** 2 vivesti vo 2 stepen
print(unique_values)
print("=======================")


# Dict comprehension

data = ['John_25', 'Sally_19', 'Susan_35', 'Jack_16']
name_age_dict = {v.split('_')[0]: v.split('_')[1] for v in data}
print(name_age_dict)
print("-----------------------")


values_squares = {value: value ** 2 for value in range(10)}
print(values_squares)
print("=======================")


# Tuple comprehension

m = tuple(n for n in range(12))
print(m)
print("=======================")


# Double Comprehension i Flattening
# Double Comprehension

matrix = [[j for j in range(2)] for i in range(3)]
print(matrix)
print("-----------------------")


# Flattening

flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)
print("=======================")


# Reshenie zadach
# ZADACHI:

# Zadacha 1:
# Napisat funkciyu, kotoraya prinimaet argument index, count i sozdaet slovar s klyuchom "ID":
# index, polem "values" kak spisok strok, sgenerirovannih v diapazone ot 0 do count diva "i_index",
# gde i - znachenie ot 0 do count, naprimer: index=1, count = 3: {"ID": 1, "values": ["0_1", "1_1",
# "2_1"]}.

def func(index, count):
    return {
        "ID": index,
        "values": ["{}_{}".format(index, value) for value in range(count)]
    }


print("-----------------------")

# Zadacha 2:
# Sdelat funkciyu, kotoraya prinimaet argument count i vizivaet funkciyu iz pervogo zadaniya i
# peredaet tuda i, j gde i - znachenie ot 0 do count, a j - znachenie ot count do 0. Poluchenniy
# slovar ona dobavlyaet v spisok, delaya spisok slovarey.


def generate(count):
    return [func(i, j) for i, j in zip(range(count), list(range(count))[::-1])]


print("-----------------------")

# Zadacha 3:
# Napisat flatten list comprehension dlya poluchennogo spiska slovarey, gde finalniy resultat budet
# spisok iz "raspakovannih" spiskov "values" v kazhdom slovare.


r = generate(9)
f = [value for sublist in r for value in sublist['values']]
print(f)

print("=======================")

array = [[1, 2], [3, 4]]

f = [x for y in array for x in y]
print(f)

# PS: Ispolzuyte tolko comprehension
# Chtobi poluchit spisok vida [(0, 9), (1, 8), (2, 7), (3, 6), ...] dlya vipolneniya 2 zadachi s
# generaciey znacheniy i, j ispolzuyte zip(range(count), list(range(count))[::-1}) i iteriruyte
# srazu i, j.