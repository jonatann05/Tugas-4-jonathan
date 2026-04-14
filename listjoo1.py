shoppingList = ['Milk', 'Cheese', 'Butter']  ## bikin list belanja

for i in range(len(shoppingList)):  ## looping pakai index
    shoppingList[i] = shoppingList[i] + "+"  ## tambahin tanda +
    print(shoppingList[i])  ## tampilkan hasil tiap item

empty = []  ## list kosong
for i in empty:  ## looping list kosong (jadi tidak jalan)
    print("I am empty")  ## tidak akan pernah dieksekusi


# =========================
# OUTPUT
# =========================

# Milk+
# Cheese+
# Butter+
# (tidak ada output untuk empty karena list kosong)