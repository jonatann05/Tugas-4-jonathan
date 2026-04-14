def f(value, values):
    v = 1
    values[0] = 44              # nilai index 0 di list diubah jadi 44

t = 3
v = [1, 2, 3]                  # list (mutable)

f(t, v)                       # t tidak berubah, tapi list v bisa berubah

print(t, v[0])                # t tetap 3, v[0] sudah berubah jadi 44


# A. 1 44
# B. 3 1
# C. 3 44 (this is the right answer)
#    karena integer (t) immutable, sedangkan list (v) mutable jadi bisa berubah
# D. 1 1