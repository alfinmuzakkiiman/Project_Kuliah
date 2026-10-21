# ========================================================
# Latihan Mandiri 2 - Operator Aritmatika
# Tugas: Konversi total detik menjadi jam, menit, dan detik
#        menggunakan operator // dan %.
# IPO:
# - Input   : total detik (int)
# - Process : jam = total // 3600
#             sisa = total % 3600
#             menit = sisa // 60
#             detik = sisa % 60
# - Output  : jam, menit, detik
# ========================================================

print("=== KONVERSI DETIK KE JAM:MENIT:DETIK ===")

# Input
total_detik = int(input("Masukkan total detik: "))

# Process
jam   = total_detik // 3600
sisa  = total_detik % 3600
menit = sisa // 60
detik = sisa % 60

# Output
print("\n" + str(total_detik), "detik =", jam, "jam", menit, "menit", detik, "detik")
