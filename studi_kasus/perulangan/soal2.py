# ========================================================
# Studi Kasus 2 - Perulangan / Iteration
# Kasus: Menghitung Jumlah (Akumulasi) Angka 1 Sampai 100
# IPO (Input - Process - Output):
# - Input   : Tidak membutuhkan input pengguna
# - Process : Inisialisasi total = 0, lalu tambahkan i (1 s/d 100)
# - Output  : Total penjumlahan deret angka 1 sampai 100
# ========================================================

print("=== MENGHITUNG PENJUMLAHAN DERET 1 SAMPAI 100 ===")

# Inisialisasi akumulator
total = 0

# Process Iterasi
for i in range(1, 101):
    total += i

# Output
print(f"Perhitungan selesai untuk 100 perulangan.")
print(f"Total penjumlahan angka 1 s/d 100 adalah: {total}")
