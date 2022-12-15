a = -1111

if -10 < a < 0:
    print("отрицательное однозначное число")
elif -100 < a < 0:
    print("отрицательное двухзначное число")
elif -1000 < a < 0:
    print("отрицательное трехзначное число")
elif a <= -1000:
    print("отрицательное четырехзначное и более число")
elif 10 > a > 0:
    print("положительное однозначное число")
elif 100 > a >= 10:
    print("положительное двухзначное число")
elif 1000 > a >= 100:
    print("положительное трехзначное число")
elif a >= 1000:
    print("положительное четырехзначное и более число")
else:
    print("значение равно 0")


checking_number = 16
positive = "четное число"
negative = "нечетное число"

print(positive if checking_number % 2 == 0 else negative)


what_this_animal = "dgfdgd"

if what_this_animal == "Meow":
    print("this is cat")
elif what_this_animal == "Bark":
    print("this is a dog")
else:
    print("what animal is that")

