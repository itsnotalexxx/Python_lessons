# Zadacha 1:
# Napisat funkciyu, kotoraya prinimaet dva argumenta - celiih chisel. Vnytri
# funkciyi delayetsya proverka tipa. Esli hotya bi odno chislo iz nih ne int,
# to vozvrashaet 1, esli oba int, to schitaetsya ih summa. Esli summa
# polozhitelnaya, to vozvrashaetsya 0, esli otricatelnaya, to -1.

def check():
    print('22')

# Zadacha 2:

def sum(a, b):
    return a + b


def check_sum(fun):
    print("start")
    print(fun)
    print("end")


check_sum(sum(2, 5))