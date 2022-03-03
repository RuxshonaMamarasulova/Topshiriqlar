               # 1-topshiriq
shaxs_0 = {
    'ism': 'Abu Abdulloh Muhammad ibn Ismoil',
    't_yil': 810,
    't_joy': 'Buxoro',
    'umr_korgan': 60,
    'asarlar': ["Al-jome' as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag'ir"]
}
shaxs_1 = {    
    'ism': 'Abulla Qodiriy',
    't_yil': 1894,
    't_joy': 'Toshkent',
    'umr_korgan': 44,
    'asarlar':["O'tkan kunlar", "Mehrobdan Chayon", "Obid ketmon"]    
}
shaxs_2 = {    
    'ism': 'Erkin Vohidov',
    't_yil': 1936,
    't_joy': 'Farg\'ona',
    'umr_korgan': 80,
    'asarlar':["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"]    
}
shaxs_3 = {    
    'ism': 'Alisher Navoiy',
    't_yil': 1441,
    't_joy': 'Xirot',
    'umr_korgan': 60,
    'asarlar':["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", "Munojot"]    
}

shaxslar = [shaxs_0, shaxs_1, shaxs_2, shaxs_3]
for shaxs in shaxslar:
    print(f"{shaxs['ism']} "
         f"{shaxs['t_yil']}-yilda "
         f"{shaxs['t_joy']}da tavallud topgan. "
         f"{shaxs['umr_korgan']} yil umr ko'rgan.")



#                # 2-topshiriq
# shaxs_0 = {
#     'ism': 'Abu Abdulloh Muhammad ibn Ismoil',
#     'asarlar': ["Al-jome' as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag'ir"]
# }
# shaxs_1 = {
#     'ism': 'Abulla Qodiriy',
#     'asarlar':["O'tkan kunlar", "Mehrobdan Chayon", "Obid ketmon"]    
# }

# shaxs_2 = {
#     'ism': 'Erkin Vohidov',
#     'asarlar':["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"]    
# }

# shaxs_3 = {
#     'ism': 'Alisher Navoiy',
#     'asarlar':["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", "Munojot"]    
# }

# shaxslar = [shaxs_0, shaxs_1, shaxs_2, shaxs_3]

# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlar']

#     print(f"\n{shaxs['ism']}ning mashxur asarlari: ")
#     for asar in asarlar:
#         print(asar)



#                # 3-topshiriq
# dostlar = {
#     'ali': ['Terminator', 'Rambo', 'Titanik'],
#     'vali': ['Qasoskorlar', 'O\'rgimchak odam', 'Tenet'],
#     'hasan': ['Abdullajon', 'Shaytanat', 'Bomba'],
#     'husan': ['Mahallada duv-duv gap', 'John Wick']
# }

# for ism, kinolar in dostlar.items():
#     print(f'\n{ism.title()}ning sevimli kinolari: ')
#     for kino in kinolar:
#         print(kino)



#                # 4-topshiriq
# davlatlar = {
#     'Ozbekiston': {
#         'poytaxt': 'Toshkent',
#         'hududi': 448978,
#         'aholisi': 33000000,
#         'pul birligi': 'so\'m'
#     },
#     'Rossiya': {
#         'poytaxt': 'Moskva',
#         'hududi': 170982246,
#         'aholisi': 144000000,
#         'pul birligi': 'rubl'
#     },

#     'AQSH': {
#         'poytaxt': 'Vashington',
#         'hududi': 9631418,
#         'aholisi': 327000000,
#         'pul birligi': 'dollar'
#     },
#     'Malayziya': {
#         'poytaxt': 'Kuala-Lumpur',
#         'hududi': 329750,
#         'aholisi': 25000000,
#         'pul birligi': 'rinngit'
#     },
# }


# for davlat, malumot in davlatlar.items(): 
#     print(f"\n{davlat}ning poytaxti {malumot['poytaxt'].title()}"
#           f"\nHududi: {malumot['hududi']} kv.km"
#           f"\nAholisi: {malumot['aholisi']}"
#           f"\nPul birligi: {malumot['pul birligi']}")




#                # 5-topshiriq
# davlatlar = {
#     'ozbekiston': {
#         'poytaxt': 'Toshkent',
#         'hududi': 448978,
#         'aholisi': 33000000,
#         'pul birligi': 'so\'m'
#     },
#     'rossiya': {
#         'poytaxt': 'Moskva',
#         'hududi': 170982246,
#         'aholisi': 144000000,
#         'pul birligi': 'rubl'
#     },

#     'aqsh': {
#         'poytaxt': 'Vashington',
#         'hududi': 9631418,
#         'aholisi': 327000000,
#         'pul birligi': 'dollar'
#     },
#     'malayziya': {
#         'poytaxt': 'Kuala-Lumpur',
#         'hududi': 329750,
#         'aholisi': 25000000,
#         'pul birligi': 'rinngit'
#     },
# }
# davlat = input('Davlat nomini kiriting: ').lower()
# if davlat in davlatlar:
#     malumot = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {malumot['poytaxt'].title()}"
#           f"\nHududi: {malumot['hududi']} kv.km"
#           f"\nAholisi: {malumot['aholisi']}"
#           f"\nPul birligi: {malumot['pul birligi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")