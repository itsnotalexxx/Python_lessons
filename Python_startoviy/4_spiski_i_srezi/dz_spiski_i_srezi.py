# Vivesti vse zhacheniya menshe 5

a = [2, 4, 65, 32, 2, 6, 0, -1, 3]
c = []
for e in a:
    if e < 5:
        c.append(e)
    else:
        continue
c.sort(reverse=True)
print(c)

print("-------------")

# Proverka polindroma

b = list("aabbaa")
print(b)
b.reverse()
print(b)

print("-------------")

# Vivesti vse elementy menshe 6

d = [1, 3, 9, 13, 7, 8, 13, 32, 44, 59, 19]
f = []
for i in d:
    if i < 6:
        f.append(i)
    else:
        continue
f.sort()
print(f)

print("-------------")

# Sozdat spisok v kotorom budet lishnie slovo iz spiska g

g = ['red', 'yellow', 'blue', 'bread']
j = []
k = g.pop(3)
print(g)
print(k)
j.append(k)
print(j)