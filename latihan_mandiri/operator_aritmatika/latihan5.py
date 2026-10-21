# ========================================================
# Latihan Mandiri 5 - Operator Aritmatika
# Tugas: Tentukan hasil ekspresi berikut secara manual,
#        lalu verifikasi dengan Python.
# ========================================================
# Penjelasan urutan operasi (precedence):
# 1. Tanda kurung () dikerjakan terlebih dahulu
# 2. Pangkat **
# 3. Perkalian *, Pembagian /, Pembagian bulat //, Modulus %
# 4. Penjumlahan +, Pengurangan -

print("=== VERIFIKASI EKSPRESI ARITMATIKA ===")
print()

# Ekspresi 1: 5 + 2 * 3
# Manual: perkalian dulu -> 2 * 3 = 6, lalu 5 + 6 = 11
print("5 + 2 * 3     =", 5 + 2 * 3)

# Ekspresi 2: (5 + 2) * 3
# Manual: kurung dulu -> 5 + 2 = 7, lalu 7 * 3 = 21
print("(5 + 2) * 3   =", (5 + 2) * 3)

# Ekspresi 3: 20 // 6
# Manual: pembagian bulat -> 20 / 6 = 3.33... dibulatkan ke bawah = 3
print("20 // 6       =", 20 // 6)

# Ekspresi 4: 20 % 6
# Manual: sisa bagi -> 20 = 6 * 3 + 2, sisa = 2
print("20 % 6        =", 20 % 6)

# Ekspresi 5: 3 ** 2 + 1
# Manual: pangkat dulu -> 3 ** 2 = 9, lalu 9 + 1 = 10
print("3 ** 2 + 1    =", 3 ** 2 + 1)
