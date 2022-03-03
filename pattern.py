# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 05:24:32 2022

@author: Khabibullayev
"""
q = input("Yangi parol qo'shing:")
w = input("Yana bir marotaba takrorlang:")
pattern = []
if len(q) < 5:
    print("Parol 5 ta harfdan ko'proq bo'lishi shart.")
else:
    print()
if q == w:
    print(f" {w} parol sifatida Laptop ga qo'shildi.Pastga parolni kiriting.")
e = input("Parolni kiriting:")
if e == w:
    print("Muvofaqiyatli yakunlandi.")
else:
    print("Noto'g'ri parol.Tekshirib,qaytadan urinib ko'ring.")
pattern.append(pattern)
