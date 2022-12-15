apples = 10
var_2 = 10000
print(id(apples))
print(id(var_2))


a = 'hello'
b = "hello"
c = '''hello world'''
d = '''Hello
        its
        a
        str'''
e = """Hello
        its
        a
        str"""

print(a)
print(b)
print(c)
print(d)
print(e)

f = "this is John`s ball"

print(f)

h = "hello"
j = "world"
k = h + j
print(k)
print(k*3)

print(len(k))

m = "abc"
print(m.upper())

s = "ABC"
print(s.lower())


aa = 2
bb = 5
cc = aa // bb
print(cc)

dd = aa ** bb
print(dd)

x = True
y = False

print(bool(0))
print(bool(-1))


counter = 0
if counter < 10:
    counter += 1
else:
    print(counter)
    