# Chto takoe rekursiya v programirovanii.

# REKURSIYA - kogda funkciya vizivaet samu sebya (prostaya rekursiya) ili kogda ona vizivaet
# samu sevya cherez druguyu funkciyu(kosvannaya rekursiya).

# Dva samih vazhnih momenta v rekursii: izmenenie sostoyaniya i uslovie vihoda.
# Esli pervoe uslovie ne soblyudeno, kod teryaet logiky, esli vtoroe uslovie ne soblyudeno,
# to budet perepolnenie steka i oshibka.


# Prostie varianti primeneniya rekursii.


a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 2, 3, 1]


def iter_arr(array):
    for elem in array:
        print(elem)


iter_arr(a)
print("---------------")


def iter_rec(array, index=0):
    if index < len(array):
        print(array[index])
        index += 1
        iter_rec(array, index)


iter_rec(b)

print("====================")

# Binarnoe derevo.
# Binarnoe derevo - eto ierarhicheskaya struktura dannih, v kotoroy kazhdiy uzel imeet znachenie
# (ono zhe yavlyaetsya v dannom sluchae i klyuchom) i ssilki na levogo i pravogo potomka. Uzel,
# nahodyashiysya na samom verhnem urovne (ne yavlyauyshiysya chiim libo potomkom) nazivaetsya
# kornem. Uzli, ne imeyushie potomkov (oba potomka kotorih ravni NULL) nazivayutsya listyami.


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


a = [4, 5, 1, 3, 2, 8, 0]

for i in range(len(a)):
    if i == 0:
        root = Node(a[i])
    else:
        root.insert(a[i])
root.print_tree()

print("====================")

# Reshenie zadach.

# Zadacha 1:
# Realizovat funkciyu poiska znacheniya v binarnom dereve. Esli znachenie naideno, to funkciya
# vernet True i predvaritelno vivedet v konsol, chto znachenie naideno, v obratnom sluchae - False
# i vivedet v konsol, chto takogo znacheniya nety.


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Vipolnenie zadachi 1 !!!!!
    def search(self, data):
        if data == self.data:
            print("{} in tree".format(data))
            return True
        if data < self.data:
            if self.left is None:
                print("{} not in tree".format(data))
                return False
            return self.left.search(data)
        if self.right is None:
            print("{} not in tree".format(data))
            return False
        return self.right.search(data)
    # Zakonchili vipolnenie zadachi 1 !!!!!

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


b = [4, 5, 1, 3, 2, 8, 0]

for i in range(len(b)):
    if i == 0:
        root2 = Node(b[i])
    else:
        root2.insert(b[i])
root2.search(8)


print("---------------")

# Zadacha 2:
# Dano naturalnoe chislo N, vivesti vse naturalnie chisla ot 1 do N.


def values(n, current=1):
    if current <= n:
        print(current)
        values(current=current + 1, n=n)


values(10)

print("---------------")

# Zadacha 3:
# Dano naturalnoe chislo N. Vivedite slovo YES, esli chislo N yavlyaetsya tochnoi ctepeniyu dvoiki,
# ili slovo NO v protivnom sluchai.


def check_pow_2(n):
    if n == 1:
        print("YES")
    else:
        if n % 2 == 0:
            check_pow_2(n // 2)
        else:
            print("NO")


check_pow_2(17)

print("---------------")

# Zadacha 4:
# Dano naturalnoe chislo N. Vichislite summu ego cifr.


def sum_val(num, res=0):
    if not num:
        return res
    res += num % 10
    num //= 10
    return sum_val(num, res)


print(sum_val(125))


print("====================")