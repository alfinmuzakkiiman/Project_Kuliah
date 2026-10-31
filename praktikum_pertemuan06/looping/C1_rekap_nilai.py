# ========================================================
# C1 - Total dan Rata-rata Nilai (Looping)
# IPO:
# - Input   : jumlah mahasiswa N (int), N nilai (float)
# - Process : total = 0; ulangi N kali: total += nilai
#             rata_rata = total / N
# - Output  : jumlah data, total nilai, rata-rata
# ========================================================
# Pseudocode:
# MULAI
#   INPUT N
#   JIKA N <= 0
#     TAMPILKAN "Jumlah harus lebih dari nol"
#   SELAIN ITU
#     total <- 0
#     ULANGI i dari 1 sampai N
#       INPUT nilai
#       total <- total + nilai
#     rata_rata <- total / N
#     TAMPILKAN N, total, rata_rata
# SELESAI
# ========================================================

print("=== TOTAL DAN RATA-RATA NILAI ===")

# Input
n = int(input("Jumlah mahasiswa: "))

# Process & Output
if n <= 0:
    print("\nJumlah mahasiswa harus lebih dari nol!")
else:
    total = 0

    for i in range(1, n + 1):
        nilai = float(input("Nilai mahasiswa ke-" + str(i) + ": "))
        total += nilai

    rata_rata = total / n

    print("\n--- Hasil ---")
    print("Jumlah data :", n)
    print("Total nilai :", total)
    print("Rata-rata   :", rata_rata)
