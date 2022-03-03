

import random as r

sinfdoshlar = ["Oyatillo", "Nodirbek", "Ozod", "Elyorbek", "Qurbonali", "Hamidillo", "Abbos", "Jaloliddin", "Xurshidbek", "Ibratillo"]
print(len(sinfdoshlar))

liverpool = []
barca = []

while len(liverpool) < 5:
    oyinchi_1 = r.choice(sinfdoshlar)
    liverpool.append(oyinchi_1)
    sinfdoshlar.remove(oyinchi_1)

while len(barca) < 5:
    oyinchi_2 = r.choice(sinfdoshlar)
    barca.append(oyinchi_2)
    sinfdoshlar.remove(oyinchi_2)

print(f"Liverpool komandasida o'yinchilari:\n{liverpool}")

print(f"\nBarcelona komandasida o'yinchilari:\n{barca}")

# sinfdoshlar = ["Oyatillo", "Nodirbek", "Ozod", "Elyorbek", "Qurbonali", "Hamidillo", "Abbos", "Jaloliddin", "Xurshidbek", "Ibratillo"]

# print(r.choice(sinfdoshlar))