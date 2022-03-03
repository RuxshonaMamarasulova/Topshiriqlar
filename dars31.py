            # 1-topshiriq

class Talaba:
    def __init__(self, ism, familiya, tyil, fanlar):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        self.fanlar = []

    def get_info(self):
        return f"{self.ism} {self.familiya} {self.bosqich}-bosqich."

    def get_age(self, yil):
        return f"{yil - self.tyil} yoshda"


class Fanlar:
    def __init__(self, matematika, ona_tili, kimyo, adabiyot):
        self.matematika = matematika
        self.ona_tili = ona_tili
        self.kimyo = kimyo
        self.adabiyot = adabiyot

    def get_matem(self):
        pass

talaba1 = Talaba("Oyatillo", "Abdullayev", 2006)
talaba1 = Talaba("Hasan", "Aliyev", 2000)
talaba1 = Talaba("Husan", "Aliyev", 1998)
talaba1 = Talaba("Olim", "Salomov", 1995)