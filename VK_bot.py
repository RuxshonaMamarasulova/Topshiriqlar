# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:35:09 2022

@author: Khabibullayev
"""
# def solve(z,r,*numbers):
#     """Solve the input"""
    
#     return r+z+sum(numbers)
# print(solve(90,90))


a = input("")
if a != 'Jaloliddin Ahmadaliyev'.lower():
    print(f"Bizda {a.title()}ning qo'shiqlari topilmadi.Qaytadan urinib ko'ring!")
else:
   w = input("")
   if w == "Sog\'indim".lower():
       # c = input("Parolni kiriting:")     
       q = input("Yangi parol qo'shing:")
       y = input("Yana bir marotaba takrorlang:")
       pattern = []
       if len(q) < 5:
           print("Parol 5 ta harfdan ko'proq bo'lishi shart.")
       else:
           print()
       if q == y:
           print(f" {y} parol sifatida Laptop ga qo'shildi.Pastga parolni kiriting.")
       e = input("Parolni kiriting:")
       if e == y:
           print("Muvofaqiyatli yakunlandi.")
       else:
           print("Noto'g'ri parol.Tekshirib,qaytadan urinib ko'ring.")
       pattern.append(pattern)
       
       import random as r
       choice = list(range(1001,20000,3))
       select = r.choice(choice)
       print("\n\n",select)
       x = int(input("consoldagi sonlarni kiriting:"))
       if x == select:
           print("""               >>> Senga bo'lgan xumorim aldab <<<\n
                   >>> Suratingga qarab ovundim <<<\n
                   >>> Bilsang yurak qilmoqda talab <<<\n
                   >>> Bugun seni juda sog'indim <<<\n
                   >>> Hasratimga dengizlar guvoh <<<\n
                   >>> Osmondagi yulduzlar guvoh <<<\n
                   >>> Sog'inishim bo'lsada gunoh <<<\n
                   >>> Bugun seni juda sogi'indim <<<\n
                   >>> Sog'indim visolingni <<<\n
                   >>> Sog'indim jamolingni <<<\n
                   >>> Sog'indim hayolingni <<<\n
                   >>> Hayolingni sog'indim <<<\n
                   >>> Sog'indim visolingni <<<\n
                   >>> Sog'indim jamolingni <<<\n
                   >>> Sog'indim hayolingni <<<\n
                   >>> Hayolingni sog'indim <<<\n
                   >>> Ko'rsam edi gul yuzlaringni <<<\n
                   >>> Mayus kulgan ul ko'zlaringni <<<\n
                   >>> Menga aytgan har so'zlaringni <<<\n
                   >>> Bugun seni juda sog'indim <<<\n
                   >>> Sochlaringni uchirar shamol <<<\n
                   >>> Kuylarmi deb surarman hayol <<<\n
                   >>> So'zim tingla ey sohibjamol <<<\n
                   >>> Bugun seni juda sog'indim <<<\n
                   >>> Sog'indim visolingni <<<\n
                   >>> Sog'indim jamolingni <<<\n
                   >>> Sog'indim hayolingni <<<\n
                   >>> Hayolingni sog'indim <<<\n
                   >>> Sog'indim visolingni <<<\n
                   >>> Sog'indim jamolingni <<<\n
                   >>> Sog'indim hayolingni <<<\n
                   >>> Hayolingni sog'indim <<<\n
                   >>> Arazingni hech qo'ymasang ham <<<\n
                   >>> Asabimga ko'p o'ynasang ham <<<\n
                   >>> Qonim ichib hech to'ymasang ham-eee <<<\n
                   >>> Bugun seni juda sog'indim <<<\n
                   >>> O'jarliging, erkaligingni <<<\n
                   >>> Jinnilarcha telbaligingni <<<\n
                   >>> Hatto o'sha qaysarligingni <<<\n
                   >>> Bugun seni juda sog'indim <<<\n
                   >>> Sog'indim visolingni <<<\n
                   >>> Sog'indim jamolingni <<<\n
                   >>> Sog'indim hayolingni <<<\n
                   >>> Hayolingni sog'indim <<<\n
                   >>> Sog'indim visolingni <<<\n
                   >>> Sog'indim jamolingni <<<\n
                   >>> Sog'indim hayolingni <<<\n
                   >>> Hayolingni sog'indim <<<""")
       else:            
           print("Qayerdadir adashyabsiz.Tekshirib qaytadan urinib ko'ring.")
       
     
   else:
       print(f"Bizda {a.title()}ning {w.title()} nomli qo'shig'i topilmadi.Tekshirib qaytadan urinib ko'ring!")