            # 1-topshiriq
buyurtmalar = []
n = 1
while True:
    savol = input(f"\n{n}-mahsulotni kiriting: \n>>>")
    buyurtma = (savol)
    buyurtmalar.append(buyurtma)
    takrorlash = input("\nYana mahsulot qo'shasizmi(ha/yo'q)? ")
    n += 1
    if takrorlash != 'ha':
        break

print("\nMahsulotlar ro'yxati:")
print(buyurtmalar)



#             # 2-topshiriq
# print("Mahsulot nomini va narhini qabul qilib konsolga chiqaruvchi dastur:")
# mahsulotlar = {}
# while True:
#     savol_0 = f"\nMahsulot nomini kiriting: "
#     savol_1 = "Mahsulot narhini kiriting: "
#     qiymat = input(savol_0)
#     narh = input(savol_1)
#     mahsulotlar[qiymat] = int(narh)
#     takrorlash = input("\nYana mahsulot kiritasizmi? (ha/yo'q) ")
#     if takrorlash != 'ha':
#         break

# royxat = input("Mahsulotlar ro'yxatini ko'rishni istaysizmi? ")
# if royxat == 'ha':
#     print("\nMahsulotlar ro'yxati:")
#     for k, q in mahsulotlar.items():
#         print(f"{k}: {q} so'm")
# else:
#     print("Dastur tugadi")




#             # 3-topshiriq
# mahsulotlar = {
#     'non': 2500,
#     'kartoshka': 7000,
#     'piyoz': 2000,
#     'guruch': 10000,
#     'go\'sh': 65000,
#     'pepsi': 9000
# }

# print("Mahsulot nomini qabul qilib narhini chiqaruvchi dastur.")
# buyurtmalar = []
# n = 1
# while True:
#     savol = input(f"\n{n}-mahsulotni kiriting:\n>>>  ")
#     buyurtma = (savol)
#     buyurtmalar.append(buyurtma)
#     takrorlash = input("\nYana mahsulot qo'shasizmi(ha/yo'q)? ")
#     n += 1
#     if takrorlash != 'ha':
#         break

# narh = input("Mahsulot narhlarini ko'rasizmi? ")

# if narh == 'ha':
#     for buyurtma in buyurtmalar:
#         if buyurtma in mahsulotlar:
#             print(f"{buyurtma} {mahsulotlar[buyurtma]} so'm")

#         else:
#             print(f"{buyurtma} yo'q")

# else:
#     print("Dastur tugadi")

