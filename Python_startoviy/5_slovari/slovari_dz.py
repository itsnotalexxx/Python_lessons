# Nayti samoe bolshoe chislo iz znacheniy slovarya

d = {"a": 3, 'b': 0, 'c': 4, "d": -3, 'e': 2}
g = 0
for key, value in d.items():
    if value > g:
        k = value
        g += 1
print(k)

# Nayti samoe bolshoe chislo iz znacheniy slovarya

e = {'a': 3, 'b': 'hello', 'c': 4, 'd': -3}
o = 0

for key, value in e.items():
    if type(value) == int:
        if value > o:
            o = value
print(o)