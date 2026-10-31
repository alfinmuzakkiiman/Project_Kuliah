# ========================================================
# B1 - Kategori Nilai Mahasiswa (Selection)
# IPO:
# - Input   : nilai akhir (float)
# - Process : validasi rentang 0-100, tentukan predikat A-E
#             A >= 85, B >= 75, C >= 65, D >= 50, E < 50
# - Output  : nilai dan predikat, atau pesan input tidak valid
# ========================================================
# Pseudocode:
# MULAI
#   INPUT nilai
#   JIKA nilai < 0 ATAU nilai > 100
#     TAMPILKAN "Input tidak valid"
#   SELAIN ITU
#     JIKA nilai >= 85: predikat <- "A"
#     JIKA nilai >= 75: predikat <- "B"
#     JIKA nilai >= 65: predikat <- "C"
#     JIKA nilai >= 50: predikat <- "D"
#     SELAIN ITU: predikat <- "E"
#     TAMPILKAN nilai, predikat
# SELESAI
# ========================================================

print("=== KATEGORI NILAI MAHASISWA ===")

# Input
nilai = float(input("Masukkan nilai akhir (0-100): "))

# Process & Output
if nilai < 0 or nilai > 100:
    print("\nInput tidak valid! Nilai harus antara 0-100.")
else:
    if nilai >= 85:
        predikat = "A"
    elif nilai >= 75:
        predikat = "B"
    elif nilai >= 65:
        predikat = "C"
    elif nilai >= 50:
        predikat = "D"
    else:
        predikat = "E"

    print("\nNilai    :", nilai)
    print("Predikat :", predikat)
