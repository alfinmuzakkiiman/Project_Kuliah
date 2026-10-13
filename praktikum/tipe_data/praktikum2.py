# ========================================================
# Praktikum 2 - Tipe Data dan Variabel
# Kasus: Input dan Konversi Tipe Data
# IPO:
# - Input   : nama (str), umur (str -> int setelah konversi)
# - Process : konversi umur ke int, hitung umur tahun depan
# - Output  : nama, umur, umur tahun depan
# ========================================================
# Penjelasan: input() selalu menghasilkan tipe data string (str).
# Fungsi int() digunakan untuk mengonversi string angka menjadi integer
# agar dapat digunakan dalam operasi aritmetika.
# Jika pengguna memasukkan teks bukan angka, akan muncul ValueError.

print("=== INPUT DAN KONVERSI TIPE DATA ===")

# Input
nama = input("Nama: ")
umur = int(input("Umur: "))  # konversi str -> int

# Process
tahun_depan = umur + 1

# Output
print("\nNama             :", nama)
print("Umur             :", umur)
print("Umur tahun depan :", tahun_depan)
