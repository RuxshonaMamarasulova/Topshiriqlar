"""Son topish o'yini"""

import random

def son_top(x = 10):
    tasodifiy_son = random.randint(1, x)
    print(f"\nMen 1 dan {x} gacha son o'yladim. Topa olasizmi?")
       
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin  = int(input(">>>"))

        if taxmin < tasodifiy_son:
            print("\nMen o'ylagan son bundan kattaroq. Yana urinib ko'ring:")
        elif taxmin > tasodifiy_son:
            print("\nMen o'ylagan son bundan kichikroq.Yana urinib ko'ring:")
        else:
            break

    print(f"Tabriklaymiz. Men o'ylagan sonni {taxminlar} ta taxmin bilan topdingiz.")
    return taxminlar



def son_top_kampyuter(x = 10):
    print("\nEndi sizni navbatingiz.")
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing men topaman.")
    pas = 1
    baland = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if pas != baland:
            taxmin = random.randint(pas, baland)
        else:
            taxmin = pas

        javob = input(f"\nSiz {taxmin} sonini o'yladingiz. To'g'ri (t),"
                    f"men o'ylagan son bundan kattaroq (+), men o'ylagan son bundan kichikroq (-):\n>>>")
        
        if javob == "+":
            pas = taxmin + 1

        elif javob == "-":
            baland = taxmin - 1

        else:
            break
    
    print(f"Men siz o'ylagan sonni {taxminlar} ta taxmin bilan topdim.")
    return taxminlar




def play(x = 10):

    while True:
        taxminlar_foydalanuvchi = son_top(x)
        taxminlar_kampyuter = son_top_kampyuter(x)

        if taxminlar_foydalanuvchi > taxminlar_kampyuter:
            print(f"\nMen yutdim. Chunki men {taxminlar_kampyuter} ta taxmin bilan topdim, siz esa {taxminlar_foydalanuvchi} ta taxmin bilan topdingiz.")

        elif taxminlar_foydalanuvchi < taxminlar_kampyuter:
            print(f"\nSiz yutdingiz. Chunki men {taxminlar_kampyuter} ta taxmin bilan topdim, siz esa {taxminlar_foydalanuvchi} ta taxmin bilan topdingiz.")

        else:
            print(f"DURRANG! Siz ham, men ham {taxminlar_foydalanuvchi} ta taxmin bilan topdik.")

        takrorlash = input("Yana o'ynaysizmi? (ha/yo'q): ")

        if takrorlash != "ha":
            break
    print("O'yin tugadi.")


print("\n'SON TOPISH' o'yiniga xush kelibsiz!!!")
print(play())



