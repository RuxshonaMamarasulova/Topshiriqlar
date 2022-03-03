            # 1-topshiriq
def katta_harf(ismlar):
    for n in range(len(ismlar)):
        ismlar[n] = ismlar[n].title()

    return ismlar


talabalar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(talabalar)
print(talabalar)



#             # 2-topshiriq
# def katta_harf(ismlar):
#     ismlar = ismlar[:]
#     for n in range(len(ismlar)):
#         ismlar[n] = ismlar[n].title()

#     return ismlar


# talabalar = ['ali', 'vali', 'hasan', 'husan']
# katta_ism = katta_harf(talabalar)
# print(katta_ism)
# print(talabalar)



#             # 3-topshiriq
# talabalar = ['ali', 'vali', 'hasan', 'husan']

# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = int(input(f"Talaba {ism.title()} ning bahosini kiriting: "))
#         baholar[ism] = baho

#     return baholar

# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)