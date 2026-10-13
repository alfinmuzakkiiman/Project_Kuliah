# ========================================================
# Studi Kasus 1 - Runtunan / Sequence
# Kasus: Menghitung Luas Permukaan dan Volume Balok
# IPO (Input - Process - Output):
# - Input   : panjang, lebar, tinggi (float)
# - Process : luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
#             volume = panjang * lebar * tinggi
# - Output  : luas permukaan balok dan volume balok
# ========================================================

print("=== MENGHITUNG LUAS PERMUKAAN & VOLUME BALOK ===")

# Input
panjang = float(input("Masukkan panjang (cm): "))
lebar = float(input("Masukkan lebar (cm): "))
tinggi = float(input("Masukkan tinggi (cm): "))

# Process
luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
volume = panjang * lebar * tinggi

# Output
print("\n--- HASIL PERHITUNGAN ---")
print("Luas Permukaan Balok =", luas_permukaan, "cm^2")
print("Volume Balok         =", volume, "cm^3")
