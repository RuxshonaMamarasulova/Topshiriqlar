            # 1-topshiriq

def kopaytir(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma

print(kopaytir(1,2))
print(kopaytir(1,2,4,5,8,10,3))
print(kopaytir(1,2,1,10,10,10))   


#             # 2-topshiriq
# def talaba_info(ism, familiya, **malumotlar):
#     malumotlar['ism'] = ism
#     malumotlar['familiya'] = familiya
#     return malumotlar

# talaba_1 = talaba_info('Oyatillo', 'Abdullayev',)
# talaba_2 = talaba_info('Oyatillo', 'Abdullayev', tugilgan_yili = 2006, telefon_raqami = 905817848)

# print(talaba_1)
# print(talaba_2)
