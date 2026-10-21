# ========================================================
# Praktikum 1 - Operator Aritmatika
# Kasus: Kalkulator Empat Operasi
# IPO:
# - Input   : bilangan pertama (float), bilangan kedua (float)
# - Process : penjumlahan, pengurangan, perkalian, pembagian
# - Output  : hasil keempat operasi
# ========================================================
# Catatan: Pembagian diperiksa terlebih dahulu apakah pembagi
# bernilai nol untuk menghindari ZeroDivisionError.

print("=== KALKULATOR EMPAT OPERASI ===")

# Input
a = float(input("Masukkan bilangan pertama: "))
b = float(input("Masukkan bilangan kedua  : "))

# Process & Output
print("\n--- Hasil Operasi ---")
print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian  :", a * b)

if b != 0:
    print("Pembagian  :", a / b)
else:
    print("Pembagian tidak dapat dilakukan karena pembagi nol.")
