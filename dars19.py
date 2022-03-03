                # 1-topshiriq
def tugilgan_yil_hisobla(ism, yosh):
    """Foydalanuvchidan ismi va yoshini qabul qilib,
    tug'ilgan yilini hisoblaydi"""
    print(f"{ism.title()} {2022-yosh}-yil tavallud topgan")

ism = input("Ismingizni kiriting: ")
yosh = int(input("yoshingizni kiriting: "))
tugilgan_yil_hisobla(ism, yosh)



#             # 2-topshiriq
# def kvadrati_va_kubini_hisobla(son):
#     """"Foydalanuvchidan qiymat qabul qilib,
#     kvadrat va kubini hisoblaydi"""
#     print(f"{son} ning kvadrati {son**2} ga teng,"
#           f"\n{son} ning kubi {son**3} ga teng")

# son = int(input("Son kiriting: "))
# kvadrati_va_kubini_hisobla(son)



#             # 3-topshiriq
# def sonni_aniqla(son):
#     """"Foydalanuvchidan son qabul qilib,
#     uni juft yoki toqligini aniqlaydi"""
#     if son%2 == 0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")

# print("Sonning juft yoki toqligini aniqlovchi dastur.")
# son = int(input("Biror son kiriting: "))

# sonni_aniqla(son)




#             # 4-topshiriq
# def kattasini_aniqla(a, b):
#     """"Foydalanuvchidan ikkita son qabul qilib,
#     kattasini aniqlaydi"""
#     if a > b:
#         print(f"{a} katta")
#     elif a < b:
#         print(f"{b} katta")
#     else:
#         print("Sonlar teng")

# print("Ikkita sondan kattasini aniqlaydigan dastur.")
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))

# kattasini_aniqla(a, b)



#             # 5-topshiriq
# def darjani_hisobla(x, y):
#     """Foydalanuvchidan son va uning darajasini qabul qilib, hisoblaydi"""
#     if y == 2:
#         print(f"{x} ning kvadrati {x**y} ga teng")
#     elif y == 3:
#         print(f"{x} ning kubi {x**y} ga teng")
#     else:
#         print(f"{x} ning {y}-darajasi {x**y} ga teng")


# print("Son va darajasini qabul qilib, hisoblaydigan dastur.")
# x = int(input("Son kiriting: "))
# y = int(input("Sonning darajasini kiriting: "))

# darjani_hisobla(x, y)



#             # 6-topshiriq
# def kvadratini_hisobla(son, kvadrat = 2):
#     """Foydalanuvchidan son qabul qilib, kvadratini hisoblaydi"""
#     print(f"{son} ning kvadrati {son**kvadrat} ga teng")

# print("Kvadratni hisoblaydigan dastur")
# son = int(input("Son kiriting: "))

# kvadratini_hisobla(son)



#             # 7-topshiriq
# def bolinish_alomatlari(son):
#     """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 ga qoldiqsiz bo'linadiganlarini aniqlaydi"""
#     for n in range(2,11):
#             if not (son%n):
#                     print(f"{son} soni {n} ga qoldiqsiz bo'linadi")


# print("2 dan 10 ga qoldiqsiz bo'linadiganlarini aniqlaydigan dastur.")
# son = int(input("Butun son kiriting: "))

# bolinish_alomatlari(son)
  

