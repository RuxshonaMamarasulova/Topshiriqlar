            # 1-topshiriq
class Foydalanuvchi:
    def __init__(self, ism, familiya, t_yil, email):
        self.ism = ism
        self.familiya = familiya
        self.email = email
        self.t_yil = t_yil

    def get_info(self):
        return f"\nFoydalanuvchi: {self.ism.title()} {self.familiya.title()} {2022 - self.t_yil} yoshda \ngmail: {self.email}@gmail.com"


ism = input("Ismingiz: ")
familiya = input("Familiyangiz: ")
t_yil = int(input("Tug'ilgan yilingiz: "))
email = input("Elektron manzilingiz: ")

foydalanuvchi = Foydalanuvchi(ism, familiya, t_yil, email)
print(foydalanuvchi.get_info())

                
