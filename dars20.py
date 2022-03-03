            # 1-topshiriq
def shaxs_info(ismi , familiyasi, t_yili, t_joyi, email_manzili = '', telefon_raqami = None):
    """Foydalanuvchidan malumotlarni qabul qilib lug'atga aylantiradigan finksiya"""
    shaxs = {
        'ism': ismi,
        'familiya': familiyasi,
        't_yil': t_yili,
        'yoshi': 2022 - t_yil,
        't_joy': t_joyi,
        'email': email_manzili,
        'telefon': telefon_raqami
    }
    return shaxs

shaxslar = []
while True:
    ism = input("Ismingiz: ")
    familiya = input("Familiyangiz: ")
    t_yil = int(input("Tug'ilgan yilingiz: "))
    t_joy = input("Tug'ilgan joyongiz: ")
    email = input("Email manzilingiz: ")
    telefon = int(input("Telefon raqamingiz: "))
    shaxslar.append(shaxs_info(ism, familiya, t_yil, t_joy, email, telefon))
    ishora = input("Yana odam qo'shasizmi? (ha/yo'q):")
    if ishora != 'ha':
        break

print('Shaxslar:')
for shaxs in shaxslar:
    print(
        f"{shaxs['ism'].title()} {shaxs['familiya'].title()},"
        f"{shaxs['yoshi']} yoshda, telefoni: {shaxs['telefon']}"
    )





#             # 2-topshiriq
# def kattasini_hisobla(a, b, c):
#     """Uchta son qabul qilib, kattasini aniqlaydigan funksiya"""
#     kattasi = a
#     if b > kattasi:
#         kattasi = b
#     if c > kattasi:
#         kattasi = c

#     return kattasi

# print("Uchta son kiriting. Bu dastur kattasini aniqlab beradi.")

# savol_1 = "1- sonni kiriting: "
# savol_2 = "2- sonni kiriting: "
# savol_3 = "3- sonni kiriting: "

# a = int(input(savol_1))
# b = int(input(savol_2))
# c = int(input(savol_3))

# max = kattasini_hisobla(a, b, c)
# print(f"{max} soni katta")


#             # 3-topshiriq
# def aylana_info(radius, pi = 3.14):
#     """Foydalanuvchidan aylana radiusini qabul qilib, aylanani radiusi, diametri, 
#     perimetri va yuzini chiqaruvchi funksiya"""
#     radius = float(radius)
#     aylana = {
#         "radius": radius,
#         "diametr": 2 * radius,
#         "perimetr": 2 * radius * pi,
#         "yuzi": pi * radius ** 2        
#     }
#     return aylana


# savol = f"Aylana radiusini kiriting: "
# radius = input(savol)
# aylana = aylana_info(radius)
# for keys, malumot in aylana.items():
#     print(f"Aylana {keys}si  {malumot}")




#             # 4-topshiriq
# def fibonachchi_son(son):
#     sonlar = []
#     for x in range(son):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1] + sonlar[x-2])
        
#         return sonlar

# savol = "Son kiriting: "
# print("\nDasturni to'xtatish uchun 'exit' deb yozing: ")
# son = int(input(savol))

# fibonachchi = fibonach
#        son = int(input(savol))
#     else:
#         break

# print(fibonachchi_son(fibonachchi))chi_son(son)
# while True:
#     if input != 'exit':