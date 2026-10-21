# ========================================================
# Latihan Mandiri 6 - Operator Aritmatika
# Tugas: Susun pseudocode dan flowchart untuk menghitung
#        rata-rata dari tiga nilai.
# ========================================================
#
# PSEUDOCODE:
# ----------------------------------------------------------
# MULAI
#     INPUT nilai1
#     INPUT nilai2
#     INPUT nilai3
#     rata_rata <- (nilai1 + nilai2 + nilai3) / 3
#     TAMPILKAN rata_rata
# SELESAI
# ----------------------------------------------------------
#
# FLOWCHART:
# ----------------------------------------------------------
#   [Mulai]
#      |
#      v
#   /Input nilai1, nilai2, nilai3/
#      |
#      v
#   [rata_rata = (nilai1 + nilai2 + nilai3) / 3]
#      |
#      v
#   /Tampilkan rata_rata/
#      |
#      v
#   [Selesai]
# ----------------------------------------------------------
# Keterangan simbol:
# [...]  = Terminator (oval) untuk Mulai/Selesai
# /.../ = Input/Output (jajar genjang)
# [...] = Process (persegi panjang) untuk perhitungan
# ========================================================

print("=== RATA-RATA TIGA NILAI ===")

# Input
nilai1 = float(input("Masukkan nilai 1: "))
nilai2 = float(input("Masukkan nilai 2: "))
nilai3 = float(input("Masukkan nilai 3: "))

# Process
rata_rata = (nilai1 + nilai2 + nilai3) / 3

# Output
print("\nNilai 1   :", nilai1)
print("Nilai 2   :", nilai2)
print("Nilai 3   :", nilai3)
print("Rata-rata :", rata_rata)
