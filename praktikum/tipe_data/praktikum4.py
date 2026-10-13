# ========================================================
# Praktikum 4 - Tipe Data dan Variabel
# Kasus: Menggabungkan Teks (String Concatenation)
# IPO:
# - Input   : nama depan, nama belakang (str)
# - Process : gabungkan dengan operator + dan spasi
# - Output  : nama lengkap
# ========================================================
# Catatan: Operator + pada tipe data string berfungsi sebagai
# penggabungan teks (concatenation), bukan penjumlahan angka.
# Perilaku operator + bergantung pada tipe data operand-nya.

print("=== PENGGABUNGAN TEKS ===")

# Input
nama_depan    = input("Nama depan    : ")
nama_belakang = input("Nama belakang : ")

# Process
nama_lengkap = nama_depan + " " + nama_belakang

# Output
print("\nNama lengkap :", nama_lengkap)
