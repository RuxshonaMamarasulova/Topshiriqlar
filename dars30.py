
class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_info(self):
        return f"{self.ism} {self.familiya} {self.bosqich}-bosqich."

    def get_age(self, yil):
        return f"{yil - self.tyil} yoshda"

talaba1 = Talaba("Oyatillo", "Abdullayev", 2006)
talaba1 = Talaba("Hasan", "Aliyev", 2000)
talaba1 = Talaba("Husan", "Aliyev", 1998)
talaba1 = Talaba("Olim", "Salomov", 1995)