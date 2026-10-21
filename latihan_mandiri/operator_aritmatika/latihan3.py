# ========================================================
# Latihan Mandiri 3 - Operator Aritmatika
# Tugas: Menghitung luas segitiga dengan rumus
#        luas = 0.5 * alas * tinggi
# IPO:
# - Input   : alas (float), tinggi (float)
# - Process : luas = 0.5 * alas * tinggi
# - Output  : luas segitiga
# ========================================================

print("=== LUAS SEGITIGA ===")

# Input
alas   = float(input("Masukkan alas   (cm): "))
tinggi = float(input("Masukkan tinggi (cm): "))

# Process
luas = 0.5 * alas * tinggi

# Output
print("\nAlas   :", alas, "cm")
print("Tinggi :", tinggi, "cm")
print("Luas   :", luas, "cm^2")
