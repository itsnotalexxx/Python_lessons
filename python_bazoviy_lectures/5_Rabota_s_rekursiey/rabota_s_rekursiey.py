# Chto takoe rekursiya v programirovanii.

# REKURSIYA - kogda funkciya vizivaet samu sebya (prostaya rekursiya) ili kogda ona vizivaet
# samu sevya cherez druguyu funkciyu(kosvannaya rekursiya).

# Dva samih vazhnih momenta v rekursii: izmenenie sostoyaniya i uslovie vihoda.
# Esli pervoe uslovie ne soblyudeno, kod teryaet logiky, esli vtoroe uslovie ne soblyudeno,
# to budet perepolnenie steka i oshibka.

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 2, 3, 1]

def iter_arr(array):
    for elem in array:
        print(elem)


def iter_rec(array, index=0):
    if index < len(array):
        print(array[index])
        index += 1
        iter_rec(array, index)


iter_arr(a)
print("---------------")
iter_rec(b)

print("====================")

# Prostie varianti primeneniya rekursii.
print("====================")

# Binarnoe derevo.
print("====================")

# Reshenie zadach.
print("====================")