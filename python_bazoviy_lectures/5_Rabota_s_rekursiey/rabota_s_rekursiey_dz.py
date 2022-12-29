# Zadacha 1:
# Napishite rekursivnuyu funkciyu, chtobi sgenerirovat i vernut spisok ot 1 do N. Argumentom
# funkciyi yavlyaetsya tolko N.


def back_list(n):
    bl = list()
    if n <= 0:
        print("need put a number more 0")
    else:
        for cur in range(n):
            if cur <= n:
                cur += 1
                bl.append(cur)
            else:
                break
        print(bl)


back_list(22)


print("-------------------")


# Zadacha 2:
# Napishite funkciyu, kotoraya rekursivno ishet v slozhnom obyekte znachenie. Slozhniy obyekt - eto
# budet spisok spiskov i spiskov. Naprimer, [1, 2, [3, 4, [5, [6 []]]]]. Funkciya dolzhna rekursivno
# zahodit vnutr vlozhennih massivov, a esli eto drugoy tip dannih ignoriryet ego.

data = [1, 2, [3, 4, [5, [6, []]]]]


def print_list(x):
    for each_item in x:
        if isinstance(each_item, list):
            print_list(each_item)
        else:
            print(each_item)


print_list(data)
