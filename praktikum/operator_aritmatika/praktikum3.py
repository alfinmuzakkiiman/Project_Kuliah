# ========================================================
# Praktikum 3 - Operator Aritmatika
# Kasus: Menghitung Pangkat
# IPO:
# - Input   : bilangan (float), pangkat (int)
# - Process : hasil = bilangan ** pangkat
# - Output  : hasil perpangkatan
# ========================================================
# Catatan: Operator ** digunakan untuk perpangkatan.
# Bilangan bukan nol dipangkatkan 0 selalu menghasilkan 1.

print("=== MENGHITUNG PANGKAT ===")

# Input
bilangan = float(input("Masukkan bilangan: "))
pangkat  = int(input("Masukkan pangkat : "))

# Process
hasil = bilangan ** pangkat

# Output
print("\nHasil perpangkatan:", hasil)
