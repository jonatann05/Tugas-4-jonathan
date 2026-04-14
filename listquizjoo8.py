def f(i, values = []):              # values default list (dipakai terus, tidak dibuat ulang)
    values.append(i)                # tiap panggilan nambah isi ke list yang sama
    print(values)                   # tampilkan isi list
    return values

f(1)            # list jadi [1]
f(2)            # lanjut dari list sebelumnya → [1, 2]
f(3)            # lanjut lagi → [1, 2, 3]


# A. [1] [2] [3]
# B. [1, 2, 3]
# C. [1] [1, 2] [1, 2, 3]  (this is the right answer)
#    karena default list di Python itu mutable dan dipakai ulang di semua pemanggilan fungsi
# D. 1 2 3