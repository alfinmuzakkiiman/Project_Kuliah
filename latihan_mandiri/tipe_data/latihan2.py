# ========================================================
# Latihan Mandiri 2 - Tipe Data dan Variabel
# Tugas: Menerima panjang dan lebar persegi panjang,
#        lalu tampilkan luasnya. Gunakan tipe data float.
# IPO:
# - Input   : panjang (float), lebar (float)
# - Process : luas = panjang * lebar
# - Output  : luas persegi panjang
# ========================================================

print("=== LUAS PERSEGI PANJANG ===")

# Input (float untuk mendukung nilai desimal)
panjang = float(input("Masukkan panjang (cm): "))
lebar   = float(input("Masukkan lebar   (cm): "))

# Process
luas = panjang * lebar

# Output
print("\nPanjang :", panjang, "cm")
print("Lebar   :", lebar,   "cm")
print("Luas    :", luas,    "cm^2")
