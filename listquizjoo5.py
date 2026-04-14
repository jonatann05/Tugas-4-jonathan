import random

fruit = ['apple', 'banana', 'papaya', 'cherry']  ## list buah

random.shuffle(fruit)  ## mengacak urutan isi list (harus pakai random.shuffle)

print(fruit)  ## tampilkan hasil setelah di-shuffle


# A. fruit.shuffle()
# B. shuffle(fruit)
# C. random.shuffle(fruit) (this is the right answer)
#    karena shuffle() ada di modul random, jadi harus dipanggil dengan random.shuffle()
# D. random.shuffleList(fruit)