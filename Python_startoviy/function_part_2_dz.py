# Zadacha 1:
# Napishite funkciyu, kotoraya menyaet znachenie globalnoy peremennoy.

varr = 10
print(varr)


def change_var():
    global varr
    varr = varr + 1


change_var()
print(varr)

# Zadacha 2:
# Napishite funkciyu dlya togo, chtobi poschitat znachenie factoriala chisla, kotoroe peredaetsya
# argumentom.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def factorial_num (x):
    total = 1
    if x == 0 or x == 1:
        x = 1
        print(x)
    elif x > 1:
        for num in range(x):
            num += 1
            total *= num
        print(total)
    else:
        pass

factorial_num(5)

# Zadacha 3:
# Naydite naybolshee znachenie v spiske s pomoshyu rekursii.

def recursion():
    list_1 = [0, 2, 3, 4, 9]
    list_2 =[]
    for x in list_1:
        if x == 0 or x == 1:
            x = 1
            list_2.append(x)
        elif x > 1:
            total = 1
            j = 0
            while x > j:
                total *= x
                x -= 1
            list_2.append(total)
        else:
            pass
    y = max(list_2)
    i = 1
    while y > i:
        y = y // i
        i += 1
    print("Найбільше значення у списку -", str(y) + '!')

recursion()