# ========================================================
# B2 - Tarif Parkir Bertingkat (Selection)
# IPO:
# - Input   : lama parkir dalam jam (int)
# - Process : jika jam < 0 -> tidak valid
#             jika jam = 0 -> biaya 0
#             jika jam >= 1 -> biaya = 5000 + (jam - 1) * 3000
# - Output  : lama parkir dan biaya parkir
# ========================================================
# Pseudocode:
# MULAI
#   INPUT jam
#   JIKA jam < 0
#     TAMPILKAN "Input tidak valid"
#   JIKA jam = 0
#     biaya <- 0
#   SELAIN ITU
#     biaya <- 5000 + (jam - 1) * 3000
#   TAMPILKAN jam, biaya
# SELESAI
# ========================================================

print("=== TARIF PARKIR BERTINGKAT ===")

# Input
jam = int(input("Lama parkir (jam): "))

# Process & Output
if jam < 0:
    print("\nInput tidak valid! Lama parkir tidak boleh negatif.")
elif jam == 0:
    biaya = 0
    print("\nLama parkir  :", jam, "jam")
    print("Biaya parkir : Rp", biaya)
else:
    biaya = 5000 + (jam - 1) * 3000
    print("\nLama parkir  :", jam, "jam")
    print("Biaya parkir : Rp", biaya)
