total = 0  ## nyimpen total semua angka
count = 0  ## nyimpen jumlah input angka

while True:  ## looping tanpa batas sampai user berhenti
    inp = input('Enter a number: ')  ## minta input dari user
    if inp == 'done': break  ## kalau input 'done', stop loop

    value = float(inp)  ## ubah input jadi angka desimal
    total = total + value  ## tambah ke total
    count = count + 1  ## tambah jumlah input

    average = total / count  ## hitung rata-rata sementara

print('Average:', average)  ## tampilkan hasil akhir


# =========================
# CONTOH INPUT
# =========================
# 10
# 20
# 30
# done

# =========================
# OUTPUT
# =========================
# Average: 20.0