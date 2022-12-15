counter = 5
while counter > 0:
    print("Iteration, counter =", counter)
    counter -= 1
print("----------")
print(counter)
print("----------")


for number in range(5):
    print(number)

print("----------")


for number in range(10):
    if number == 3:
        continue
    print(number)

print("----------")


for number in range(10):
    if number == 3:
        break
    print(number)

print("----------")


for number in range(101):
    if number % 2 == 0:
        print(number)

print("----------")


counter = 0
end_value = 101

while counter < end_value:
    if counter % 2 == 0:
        print(counter)
    counter += 1

print("----------")


word = "hello"
for char in word:
    if char == "l":
        print("s")
    else:
        print(char)

print("----------")


back_counter = 99
end_values = 0

while back_counter > end_values:
    if back_counter % 5 == 0:
        print(back_counter)
    back_counter -= 1

