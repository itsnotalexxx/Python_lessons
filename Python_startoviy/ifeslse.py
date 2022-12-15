animal = 'bird'

if animal == 'cat':
    print("Meow")
elif animal == 'dog':
    print("Wof")
elif animal == 'bird':
    print("tweet")
else:
    print("I dont know this animal")


value = 10
result_value_greater_than_zero = True if value > 0 else False
print(result_value_greater_than_zero)


product_price = 90
if product_price > 1000:
    product_price *= 0.9
elif product_price > 500:
    product_price *= 0.95
elif product_price > 100:
    product_price *= 0.97

print(product_price)


value_str = ""
print(None if not value_str else value_str)


first_value = 4
second_value = 5
operator = "+"

if first_value is None or second_value is None:
    print("Cant divide None value")
else:
    if operator == "+":
        print(first_value + second_value)
    elif operator == "-":
        print(first_value - second_value)
    elif operator == "/":
        print(first_value / second_value)
        if second_value == 0:
            print("cant divide by 0")
        else:
            print(first_value / second_value)
    elif operator == "*":
        print(first_value * second_value)
    else:
        print("Operator is wrong. Choose from given: + - / *")

