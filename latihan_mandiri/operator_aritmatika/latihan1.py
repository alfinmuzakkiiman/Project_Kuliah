# ========================================================
# Latihan Mandiri 1 - Operator Aritmatika
# Tugas: Buat program yang menerima dua angka dan menampilkan
#        hasil +, -, *, /, //, dan % dengan validasi pembagi nol.
# IPO:
# - Input   : dua angka (float)
# - Process : 6 operasi aritmatika + validasi pembagi nol
# - Output  : hasil setiap operasi
# ========================================================

print("=== ENAM OPERASI ARITMATIKA ===")

# Input
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua  : "))

# Process & Output
print("\n--- Hasil Operasi ---")
print(a, "+",  b, "=", a + b)
print(a, "-",  b, "=", a - b)
print(a, "*",  b, "=", a * b)

if b != 0:
    print(a, "/",  b, "=", a / b)
    print(a, "//", b, "=", a // b)
    print(a, "%",  b, "=", a % b)
else:
    print("Pembagian (/, //, %) tidak dapat dilakukan karena pembagi nol.")
