# ========================================================
# Studi Kasus 5 - Perulangan / Iteration
# Kasus: Menampilkan Tabel Perkalian Angka 7 (dari 1 s/d 10)
# IPO (Input - Process - Output):
# - Input   : Angka pengali (konstanta 7)
# - Process : Perulangan for i in range(1, 11), hasil = 7 * i
# - Output  : Format tabel perkalian 7 x i = hasil
# ========================================================

print("=== TABEL PERKALIAN 7 ===")
ANGKA = 7

# Process & Output
for i in range(1, 11):
    hasil = ANGKA * i
    print(f"{ANGKA} x {i:>2} = {hasil:>2}")

print("=========================")
