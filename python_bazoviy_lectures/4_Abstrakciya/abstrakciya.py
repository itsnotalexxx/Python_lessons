# PLAN UROKA

# Chto takoe ABSTRAKCIYA?

# ABSTRAKCIYA - eto sposob predstavit konechniy product takim obrazom, chtobi polzovatelyu ne
# nuzhno bilo znat kak imenno product rabotaet, no polzovatel mog im bi legko polzovatsya.
# Osnovnaya ideya sostoit v tom, chtobi otdelit sposob ispolzovaniya sostavnih obyektov dannih
# ot detaley ih realizaciyi v vide bolee prostih obyektov.

# ABSTRAKCIYA V PYTHON:

print("--------------")

# Kak na praktike one primenima.


class Core:
    def __init__(self):
        self._types = {
            "A": 100,
            "B": 300
        }

    def get_salary(self, class_name):
        return self._types.get(class_name, 0) # esli net takogo classa, vozvrashaem 0


class AccountingInterface:
    def __init__(self, data):
        self._core = Core()
        self._database = data

    def get_salary(self, name):
        class_of_employee = self._database.get(name) # polychem class sotrudnika
        salary = self._core.get_salary(class_of_employee) # polychaem zarplaty etogo sotrudnika
        return salary


db = {
    "John": "A",
    "Mike": "B"
}
interface = AccountingInterface(data=db)
print("John`s salary is: {}".format(interface.get_salary(name="John")))

print("--------------")

# Reshenie zadach.

# ZADACHA:
# Neobhodimo realizovat konsolnoe prilozhenie "kalkulyator". Polzovatel vvodit v konsol odnoi
# strokoi chislo, operator i vtoroe chislo, razdelyaya ih probelom. Chisla mogut but veshestvennie
# i celie. Kalkulyator dolzhen vipolnyat funkciyi: slozheniya(+), vichitaniya(-), deleniya(/) i
# umnozheniya(*).
# Primeri: "2 + 2", "3 / 12.5", "45 * -0.3".

# P.S: zadacha odna, no na nei nuzhno primenit vse znaniya, poluchennie na 4 urokah po nasledovaniyu,
# inkapsulyaciyi, polimorphizmy i abstrakciyi.


class Parser:
    def __init__(self):
        pass

    @staticmethod
    def __convert_types(value_str):
        result = 0
        if isinstance(value_str, str):
            if "." in value_str:
                result = float(value_str)
            else:
                result = int(value_str)
        return result

    def parse(self, expression):
        packed_values = tuple(expression.split(" "))
        if len(packed_values) < 3:
            print("Wrong indentation, check your expression")
            return 0, 0, "+"
        a, op, b = packed_values
        return self.__convert_types(a), self.__convert_types(b), op


class Coree:
    def __init__(self):
        self._parser = Parser()
        self._function = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: a / b,
            "*": lambda a, b: a * b
        }

    def calculate(self, expression):
        a, b, op = self._parser.parse(expression)
        result = self._function.get(op)(a, b)
        return result


class Interface:
    def __init__(self):
        self._coree = Coree()

    def run_calculator(self):
        while True:
            print("Enter your expression: eg. '2 + 2' ")
            expression = input()
            result = self._coree.calculate(expression)
            print("Result: {}".format(result))
            print("="*10)


if __name__ == "__main__":
    calculator = Interface()
    calculator.run_calculator()


print("--------------")


