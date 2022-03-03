            # 1-topshiriq
class Avto:
    def __init__(self, kompaniya, model, rang, karobka, narh):
        self.kompaniya = kompaniya
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.km = 0

    def get_info(self):
        return f"{self.rang} {self.model} {self.kompaniya} {self.km} {self.karobka} {self.narh}$"

    def set_km(self, yangi_km):
        self.km = yangi_km

avto1 = Avto("CHEVROLET", "malibu", "qora", "avtomat", 30000)
avto2 = Avto("WOLVO", "matiz", "sariq", "mexanik", 7000)
avto3 = Avto("GM", "toyota", "qizil", "avtomat", 35000)

km = avto1.set_km(2000)
km = avto2.set_km(1000)
km = avto3.set_km(2500)

print(avto1.get_info())
print(avto2.get_info())
print(avto3.get_info())



            # 2-topshiriq
class Avtosalon:
    def __init__(self, nomi,):
        self.nomi = nomi
        self.avtomobillar_soni = 0
        self.avtomobillar = []

    def add_avto(self, avto):
        self.avtomobillar.append(avto)
        self.avtomobillar_soni += 1

    def get_avtomobillar(self):
        return [avto.Avto.get_info() for avto in self.avtomobillar]

avtosalon = Avtosalon("General motors")

avto1 = Avto("CHEVROLET", "malibu", "qora", "avtomat", 30000)
avto2 = Avto("WOLVO", "matiz", "sariq", "mexanik", 7000)
avto3 = Avto("GM", "toyota", "qizil", "avtomat", 35000)

avtosalon.add_avto(avto1)
avtosalon.add_avto(avto2)
avtosalon.add_avto(avto3)

print("\n",avtosalon.nomi)
print(avtosalon.avtomobillar_soni)
print(avtosalon.get_avtomobillar())