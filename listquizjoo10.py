fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']  

fruit_list2 = fruit_list1          # referensi ke list yang sama (alias)
fruit_list2 = fruit_list1          # masih tetap referensi yang sama
fruit_list3 = fruit_list1[:]       # copy list baru (beda memori)

fruit_list2[0] = 'Guava'           # karena sama, fruit_list1 ikut berubah
fruit_list3[1] = 'Kiwi'            # hanya fruit_list3 yang berubah

sum = 0

for ls in (fruit_list1, fruit_list2, fruit_list3):   # cek 3 list
    if ls[0] == 'Guava':          # kalau index 0 = Guava
        sum += 1
    if ls[1] == 'Kiwi':           # kalau index 1 = Kiwi
        sum += 20

print(sum)   # hasil akhir


# =========================
# PENJELASAN HASIL LIST
# =========================
# fruit_list1 = ['Guava', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = ['Guava', 'Berry', 'Cherry', 'Papaya']
# fruit_list3 = ['Apple', 'Kiwi', 'Cherry', 'Papaya']


# =========================
# PERHITUNGAN
# =========================
# list1 → Guava di index 0 → +1
# list2 → Guava di index 0 → +1
# list3 → Kiwi di index 1 → +20
# total = 22


# A. 22 (this is the right answer)
# B. 21
# C. 0
# D. 43