            # 1-topshiriq
savol = f'Yoqtirgan kitobingiz nomini kiriting'
savol += "(Dasturni to'xtatish uchun 'stop' deb yozing):\n>>>"
ishora = True
while ishora:
    javob = input(savol)
    if javob == 'stop':
        ishora = False
    else:
        print(javob)
print('Dastur tugadi')


#             # 2-topshiriq
# print("Muzeyga chipta narxini chiqaruvchi dastur. Dasturni to'xtatish uchun \n 'exit' yoki 'quit' deb yozing")
# savol = f'Yoshingiz kiriting:\n>>>'
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         ishora = False
#         continue

#     yosh = int(qiymat)

#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta narhi {narh} so'm")

# print("Dastur tugadi")



#             # 3-topshiriq
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): \n>>>"

# while True:
#     qiymat = input(savol)

#     if float(qiymat) < 0:
#         continue
#     elif qiymat == 'exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")