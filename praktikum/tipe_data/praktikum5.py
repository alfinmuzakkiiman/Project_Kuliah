# ========================================================
# Praktikum 5 - Tipe Data dan Variabel
# Kasus: Mengatasi Kesalahan Tipe Data (Type Error)
# ========================================================
# Kode yang SALAH:
#   umur = input("Umur: ")
#   print("Tahun depan: " + (umur + 1))   # TypeError!
#
# Penyebab: input() menghasilkan str, tidak bisa dijumlahkan
# dengan int (1) secara langsung -> TypeError.
#
# Perbaikan: konversi input ke int() terlebih dahulu.
# ========================================================

print("=== MENGATASI KESALAHAN TIPE DATA ===")

# Input dengan konversi yang benar (str -> int)
umur = int(input("Umur: "))

# Output - perbaikan dari kode yang salah
print("Tahun depan:", umur + 1)

# Alternatif: jika hanya ingin menampilkan teks gunakan str()
print("Umur saat ini: " + str(umur) + " tahun")
