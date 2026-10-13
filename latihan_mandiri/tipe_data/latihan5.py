# ========================================================
# Latihan Mandiri 5 - Tipe Data dan Variabel
# Tugas: Perbaiki kode berikut agar menghasilkan angka 15:
#        angka = input("Masukkan angka: ")
#        print(angka + 5)
#
# Masalah: input() menghasilkan str, tidak bisa dijumlahkan
#          langsung dengan int (5). Akan muncul TypeError.
#
# Solusi: konversi hasil input() ke int() sebelum operasi.
# ========================================================

print("=== PERBAIKAN KESALAHAN TIPE DATA ===")

# Kode yang diperbaiki
angka = int(input("Masukkan angka: "))  # konversi str -> int
print("Hasil          :", angka + 5)   # contoh: input 10 -> output 15
