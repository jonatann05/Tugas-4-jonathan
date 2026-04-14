data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]         # list bersarang (nested list)

def fun(m):                                         # fungsi dengan parameter m
    v = m[0][0]                                     # ambil nilai awal (elemen pertama)

    for row in m:                                   # loop tiap sub-list
        for element in row:                         # loop tiap elemen di dalam sub-list
            if v < element:                         # kalau ketemu nilai lebih besar
                v = element                         # update v jadi nilai terbesar

    return v                                        # return nilai terbesar yang ditemukan

print(fun(data[0]))                                 # ambil data[0] = [[1,2],[3,4]]


# A. 1
# B. 2
# C. 3
# D. 4 (this is the right answer)
#    karena dari [1,2,3,4] nilai terbesar adalah 4
# E. 5
# F. 6