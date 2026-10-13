# ========================================================
# Latihan Mandiri 3 - Tipe Data dan Variabel
# Tugas: Menerima dua angka dan menampilkan hasil
#        penjumlahan, pengurangan, perkalian, dan pembagian.
# IPO:
# - Input   : angka1, angka2 (float)
# - Process : 4 operasi aritmetika dasar
# - Output  : hasil masing-masing operasi
# ========================================================

print("=== OPERASI ARITMETIKA ===")

# Input
angka1 = float(input("Masukkan angka pertama : "))
angka2 = float(input("Masukkan angka kedua   : "))

# Process
hasil_tambah = angka1 + angka2
hasil_kurang = angka1 - angka2
hasil_kali   = angka1 * angka2
hasil_bagi   = angka1 / angka2 if angka2 != 0 else "Tidak bisa dibagi nol"

# Output
print("\n--- Hasil Operasi ---")
print(angka1, "+", angka2, "=", hasil_tambah)
print(angka1, "-", angka2, "=", hasil_kurang)
print(angka1, "x", angka2, "=", hasil_kali)
print(angka1, "/", angka2, "=", hasil_bagi)
