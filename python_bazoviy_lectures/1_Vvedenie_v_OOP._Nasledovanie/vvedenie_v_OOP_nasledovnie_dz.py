# Zadacha 1:
# Napisat class Cat, sozdat emy atributi  size, color, cat_type.

# Zadacha 2:
# Pri sozdanii obyekta klassa peredavat v konstryktor color i cat_type, kotorie zapisivayutsya
# v sootvetstvyuyshie atribyti.

# Zadacha 3:
# Sdelat metod set_size, v kotorom esli self.cat_type eto "indoor", to self.size = "small"
# inache self.size = "undefined". Protestiryite raznie varianti.

# Zadacha 4:
# Sdelat class Tiger, unasledovaniy ot classa Cat.

# Zadacha 5
# Pereopredelit metod set_size takim obrazom chtobi esli self.cat_type eto "wild", to
# self.size = "big" inache self.size = "undefined".

class Cat:
    def __init__(self, size, color, cat_type):
        self.size = size
        self.color = color
        self.cat_type = cat_type

    @staticmethod
    def set_size(cat_type):
        if cat_type == "indoor":
            size = "small"
        else:
            size = "undefined"

        print("Cat type {}, size is {}".format(
            cat_type,
            size,
        ))

    def return_cat(self):
        print("Cat have size is {}, he is {} and him type {}".format(
            self.size,
            self.color,
            self.cat_type
        ))


this_is_cat = Cat(size="big", color="grey", cat_type="British")
this_is_cat.return_cat()
Cat.set_size("dgd")


class Seam(Cat):
    def __init__(self, size, color, cat_type):
        Cat.__init__(self, size, color, cat_type)

    def return_cat_color_and_type(self):
        print("This cat have color is {} and type {}".format(
            self.color,
            self.cat_type
        ))


seam_cat = Seam(size="small", color="black", cat_type="Seam")
seam_cat.return_cat_color_and_type()


class Tiger(Cat):
    def __init__(self, size, color, cat_type):
        Cat.__init__(self, size, color, cat_type)

    @staticmethod
    def set_size(cat_type):
        if cat_type == "wild":
            size = "Big"
        else:
            size = "undefined"

        print("Cat type {}, size is {}".format(
            cat_type,
            size
        ))


tiger = Tiger(size="small", color="orange", cat_type="pet")
tiger.set_size("fgf")