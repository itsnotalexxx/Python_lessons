# fibonachi number
num3 = 0
num4 = 1

for i in range(10):
    num5 = num4 + num3
    num3 = num4
    num4 = num5
    print(num5)

print("----------")

words = "Hello world"

for char in words:
    if char == "o":
        print("a")
    elif char == "l":
        print("e")
    else:
        print(char)

print("----------")

phrase = "Ham is tasty"
i = 0
for char in phrase:
    i += 1
    if char == "a" and i % 2 == 0:
        print("b")
    elif i % 2 != 0:
        print("_")
    else:
        print(char)

print("----------")

stcntr = 0
endcntr = 30
while stcntr < endcntr:
    if stcntr % 3 == 0:
        print(stcntr)
    stcntr += 1

print("----------")

for stnm in range(30):
    if stnm == 4:
        continue
    elif stnm == 18:
        break
    else:
        print(stnm)

print("----------")