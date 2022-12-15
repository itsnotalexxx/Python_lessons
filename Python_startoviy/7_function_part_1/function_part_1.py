# Ponyatiya funkciyi

# Funkciya - eto obyekt, kotoriy prinimaet i vozvrashaet znachenie. Funkciyu
# mozhno vizvat iz lyubogo mesta v kode dlya povtornogo ispolzovaniya. Eta
# koncepciya pomogaet izbezhat povtoryayushihsya uchastkov koda, a takzhe
# razbivat programy na podprogrami, chto uluchshaet chitaemost koda.


# Sozdanie funkciyi

# sintaksis: def mu_function():

def print_value():
    print(2 + 2)

# Vizov funkciyi

print(print_value)

# Peredacha parametrov v funkciyu

def func(a):
    print(a * 70)


func(2)

def func2(a, b, c):
    print(a + b + c)


func2(2, 5, 3)

# Vozvrat resultatov v funkciyu

def function(a, b):
    return a + b


result = function(2, 5)
result2 = function(10, 45)
print(result)
print(result2)

# Primeri raboti s funkciyami

# 1. Nayti maksimalnoe znachenie v peredavaemom v funkciyu spiske i vernite ego,
# esli ono bolshe 0, v inom sluchae vernite soobshenie , chto chislo menshe 0.

def get_max_from_list(list_values):
    max_value = list_values[0]
    for element in list_values:
        if element > max_value:
            max_value = element
    return max_value if max_value > 0 else "Max value is less then zero"


a = [1, 3, 56, 45, 0]
b = [-45, -2, -5, -7, -78]
max_a = get_max_from_list(a)
max_b = get_max_from_list(b)
print(max_a)
print(max_b)

# 2. Vernite kolichestvo bukv v slove, kotoroe peredaetsya v parametrah.

def get_string_length(string):
    return len(string)


string_a = "hello"
string_b = "bye"
len_a = get_string_length(string_a)
len_b = get_string_length(string_b)
print("Str a has", len_a, "characters")
print("Str b has", len_b, "characters")

# 3. Napishite funkciyu, kotoraya vozvodiit v stepen chislo, kotoroe peredaetsya
# v parametrah, esli stepen ne otricatelnaya. Perviy parametr - chislo, vtoroy -
# - stepen, v kotoruyu ego nuzhno vozvesti.

def power(value, value_power):
    if value_power >= 0:
        return value ** value_power
    else:
        return "Your value_power less then 0"


two_in_power_of_ten = power(2, -1)
print(two_in_power_of_ten)
