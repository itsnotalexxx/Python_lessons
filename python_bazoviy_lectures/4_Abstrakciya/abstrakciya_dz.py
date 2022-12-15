# ZADACHI:

# ZADACHA 1:
# Organizuite arhitekturu prilozheniya "Baza dannih"(psevdo). V roli bazi dannih u vas budet class
# Database, kotoriy budet hranit dannie v vide peremennoy spiska.

# ZADACHA 2:
# Class Database dolzhen imet metodi read_data(criteria), write_data(element).

# ZADACHA 3:
# Dlya elementa dannih napishite class Data. V dannom sluchae mi budem hranit dannie o polzovatelyah.
# Data budet imet atributi: country, name, age, gender, height, weight.

# ZADACHA 4:
# V classe Database metod read_data budet prinimat na vhod argument criteria, kotoriy yavlyaetsya
# slovarem vide {"age": 25}, posle chego metod vernet otdelniy spisok vseh elementov y kotorih
# dannoe uslovie istino.

# PODSKAZKA: chtobi poluchit u obyekta classa znachenie ego atributa kak u slovarya, ispolzuyte
# sleduyushiy sintaksis: your_class_instance._dict_get("name").

# P.S.: organizuyte pravilnuyu inkapsulyaciyu. Vi dolzhni dobavlyat elementy v class Database tolko
# cherez metod write, no nikak ne napryamuyu cherez atribut elements.


# class Database:
#     def __init__(self):
#         self._data_base = []
#
#     def read_data(self):
#         self.criteria = {"age": 25}
#
#
#     def write_data(self, element):
#         pass
#
#
# class Data:
#     def __init__(self, country, name, age, gender, height, weight):
#         self._country = country
#         self._name = name
#         self._age = age
#         self._gender = gender
#         self._height = height
#         self._weight = weight
#
#
#
# if __name__ == "__main__":
#    data1 = Data("Ukraine", "Alex", 35, "male", 181, 95)
#    data2 = Data("Russia", "Romeo", 25, "male", 193, 80)
#    data3 = Data("Poland", "Bjeshko", 29, "male", 178, 76)
#    data4 = Data("England", "Linda", 25, "female", 168, 55)
#    data5 = Data("USA", "Andrew", 15, "male", 186, 85)
#
# Database().read_data()


class Database:
    database = []

    def read_data(self, criteria={"age": 25}):
        [print(i) for i in self.database if i[2] == criteria.get("age")]

    def write_data(self, element):
        self.database.append(element)


class Data:
    def __init__(self, country, name, age, gender, height, weight):
        self.data = Database()
        element = tuple((country, name, age, gender, height, weight))
        self.data.write_data(element)


if __name__ == "__main__":
    data1 = Data("Ukraine", "Alex", 35, "male", 181, 95)
    data2 = Data("Russia", "Romeo", 25, "male", 193, 80)
    data3 = Data("Poland", "Bjeshko", 29, "male", 178, 76)
    data4 = Data("England", "Linda", 25, "female", 168, 55)
    data5 = Data("USA", "Andrew", 15, "male", 186, 85)

Database().read_data()
