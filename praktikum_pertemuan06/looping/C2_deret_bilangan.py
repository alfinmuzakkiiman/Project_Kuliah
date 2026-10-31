# ========================================================
# C2 - Deret Bilangan dan Jumlahnya (Looping)
# IPO:
# - Input   : N sebagai bilangan bulat > 0
# - Process : tampilkan deret 1 sampai N, jumlahkan seluruhnya
# - Output  : deret angka dan jumlah deret
# ========================================================
# Pseudocode:
# MULAI
#   INPUT N
#   JIKA N <= 0
#     TAMPILKAN "Input harus > 0"
#   SELAIN ITU
#     jumlah <- 0
#     ULANGI i dari 1 sampai N
#       TAMPILKAN i
#       jumlah <- jumlah + i
#     TAMPILKAN jumlah
# SELESAI
# ========================================================

print("=== DERET BILANGAN DAN JUMLAHNYA ===")

# Input
n = int(input("Masukkan nilai N: "))

# Process & Output
if n <= 0:
    print("\nInput harus lebih dari 0!")
else:
    jumlah = 0

    print("\nDeret:", end=" ")
    for i in range(1, n + 1):
        print(i, end=" ")
        jumlah += i

    print("\nJumlah deret:", jumlah)
