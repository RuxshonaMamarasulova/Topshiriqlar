                # 1-topshiriq
son = int(input('Juft son kiriting:\n>>>'))
if son%2 == 0:
        print('Rahmat')
else:
        print('Bu son juft emas')


#                 # 2-topshiriq
# print('Muzeyga xush kelibsiz!!!')
# yosh = int(input('Yoshingiz nechchida?\n>>>'))
# if yosh <= 4 or yosh > 60:
#         print('Sizga kirish bepul')
# elif yosh <= 18:
#         print('Sizga kirish 10000 so\'m')
# else:
#         print('Sizga kirish 20000 so\'m')



#                 #  3-topshiriq
# print('Istalgan ikkita son ayting')
# a = float(input('1-sonni kiriting:\n>>>'))
# b = float(input('2-sonni kiriting:\n>>>'))
# if a > b:
#         print(f'{a} > {b}')
# elif a < b:
#         print(f'{b} < {a}')
# else:
#         print(f'{a} = {b}')



#                 # 4-topshiriq
# mahsulotlar = ['non', 'piyoz', 'kartoshka', 'sabzi', 'sholg\'om', 'karam', 'shakar', 'kofe', 'guruch', 'lag\'mon']
# savat = []
# print('Savatga  beshta mahsulot kiriting.')
# for n in range(5):
#         savat.append(input(f'{n+1}-mahsulotni kiriting:\n>>>'))
# for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#                 print(f"Do'konimizda {mahsulot} bor")
#         else:
#                 print(f"Kechirasiz do'lonimizda {mahsulot} yo'q")



#                 # 5-topshiriq
# mahsulotlar = ['non', 'piyoz', 'kartoshka', 'sabzi', 'sholg\'om', 'karam', 'shakar', 'kofe', 'guruch', 'lag\'mon']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# print('Savatga  beshta mahsulot kiriting.')

# for n in range(5):
#         savat.append(input(f'{n+1}-mahsulotni kiriting:\n>>>'))

# for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#                 bor_mahsulotlar.append(mahsulot)
#         else:
#                 mavjud_emas.append(mahsulot)

# if mavjud_emas:
#         print('Do\'konimizda quidagi mahsulotlar yo\'q:')
#         for mahsulot in mavjud_emas:
#                 print(mahsulot)
# else:
#         print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor')



#                 # 6-topshiriq
# foydalanuvchilar = ["oyatillo", "nodirbek", "xurshidbek", "abbos", "fazliddin"]
# foydalanuvchi = input('Yangi login tanlang: ')
# if foydalanuvchi.lower() not in foydalanuvchilar:
#         print(f"Xush kelibsiz {foydalanuvchi.title()}")
# else:
#         print("Login band, yangi login tanlang")


#                 # 7-topshiriq
# son = int(input("Butun son kiriting:\n>>>"))
# for n in range(2,11):
#         if not (son%n):
#                 print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
