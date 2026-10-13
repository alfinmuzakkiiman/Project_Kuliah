# ========================================================
# Studi Kasus 3 - Perulangan / Iteration
# Kasus: Menampilkan Bilangan Genap dari 2 Sampai 20
# IPO (Input - Process - Output):
# - Input   : Tidak membutuhkan input pengguna
# - Process : Perulangan dengan range(2, 21, 2) [start=2, stop=21, step=2]
# - Output  : Bilangan genap 2, 4, 6, 8, ..., 20
# ========================================================

print("=== MENAMPILKAN BILANGAN GENAP (2 - 20) ===")

# Process & Output
for i in range(2, 21, 2):
    print(i, end=" ")

print("\n\nSelesai menampilkan bilangan genap.")
