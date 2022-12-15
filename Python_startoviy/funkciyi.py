# Ponyatie funkciyi

# Sozdanie funkciyi

def print_value():
    print(2 + 2)

# Vizov funkciyi

print(print_value)

# parametri funkciyi

def func(a):
    print(a * 70)


func(2)

def func2(a, b, c):
    print(a + b + c)


func2(2, 6, 10)

# Vozvrat resultatov funkciyi

def function(a, b):
    return a + b


result = function(2, 5)
result2 = function(10, 55)
print(result)
print(result2)

# Priveri raboti funkciyi:

# 1. Nayti maksimalnoe znachenie v peredavaemom v funkciyu spiske i vernite ego, esli ono
# bolshe 0, v inom slychae vernite soobsheniye o tom, chto chislo menshe 0

def get_max_from_list(list_values):
    max_values = list_values[0]
    for element in list_values:
        if element > max_values:
            max_values = element
        return max_values if max_values > 0 else "Max value less then 0"


a = [1, 3, 56, 45, 0]

max_a = get_max_from_list(a)
print(max_a)