# Zadacha 1:
# Napishite rekursivnuyu funkciyu, chtobi sgenerirovat i vernut spisok ot 1 do N. Argumentom
# funkciyi yavlyaetsya tolko N.


bl = list()


def back_list(n):
    if n == 0:
        return n
    else:
        if n >= 1:
            bl.append(n)
            back_list(n - 1)
            bl.sort()


back_list(5)
print(bl)

print("-------------------")


# Zadacha 2:
# Napishite funkciyu, kotoraya rekursivno ishet v slozhnom obyekte znachenie. Slozhniy obyekt - eto
# budet spisok spiskov i spiskov. Naprimer, [1, 2, [3, 4, [5, [6 []]]]]. Funkciya dolzhna rekursivno
# zahodit vnutr vlozhennih massivov, a esli eto drugoy tip dannih ignoriryet ego.

spisok = [1, 2, [3, 4, [5, [6, []]]]]
cl = list()


def check_spisok(cs, level=1):
    print(cs, 'Вкладеність', level, 'рівня')
    for i in cs:
        if type(i) == list:
            check_spisok(i, level + 1)
        else:
            cl.append(i)


check_spisok(spisok)
print(cl)