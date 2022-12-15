# ZADACHI:

# ZADACHA 1:
# Napisat class User, u nego budut v konstruktore opredelyatsya polya age, name, user_type, a
# metod budet access_database.

# ZADACHA 2:
# Sdelat metod takim, chtobi esli self.user_type bil raven "superuser", to metod vivodil v konsol
# "access granted", v sluchae esli eto prosto user, to vivodilo "access denied".

# ZADACHA 3:
# Dlya superuser sdelat unasledovaniy class SuperUser ot User.


class User:
    def __init__(self, age, name, user_type):
        self._age = age
        self._name = name
        self._user_type = user_type

    def access_database(self):
        if self._user_type == "superuser":
            print("access granted")
        else:
            print("access denied")


class SuperUser(User):
    pass


u = User(age=30, name="Bob", user_type="user")
u.access_database()
su = SuperUser(age=25, name="Alex", user_type="superuser")
su.access_database()
