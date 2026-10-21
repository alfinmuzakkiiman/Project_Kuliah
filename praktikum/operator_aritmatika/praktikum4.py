# ========================================================
# Praktikum 4 - Operator Aritmatika
# Kasus: Luas dan Keliling Persegi Panjang
# IPO:
# - Input   : panjang (float), lebar (float)
# - Process : luas = panjang * lebar
#             keliling = 2 * (panjang + lebar)
# - Output  : luas dan keliling
# ========================================================

print("=== LUAS DAN KELILING PERSEGI PANJANG ===")

# Input
panjang = float(input("Panjang: "))
lebar   = float(input("Lebar  : "))

# Process
luas     = panjang * lebar
keliling = 2 * (panjang + lebar)

# Output
print("\nLuas    :", luas)
print("Keliling:", keliling)
