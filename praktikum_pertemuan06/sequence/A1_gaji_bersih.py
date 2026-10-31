# ========================================================
# A1 - Perhitungan Gaji Bersih (Sequence)
# IPO:
# - Input   : gaji pokok, tunjangan transportasi, potongan tetap
# - Process : gaji_kotor = gaji_pokok + tunjangan
#             gaji_bersih = gaji_kotor - potongan
# - Output  : gaji kotor dan gaji bersih
# ========================================================
# Pseudocode:
# MULAI
#   INPUT gaji_pokok
#   INPUT tunjangan
#   INPUT potongan
#   gaji_kotor <- gaji_pokok + tunjangan
#   gaji_bersih <- gaji_kotor - potongan
#   TAMPILKAN gaji_kotor, gaji_bersih
# SELESAI
# ========================================================

print("=== PERHITUNGAN GAJI BERSIH ===")

# Input
gaji_pokok = float(input("Gaji pokok             : "))
tunjangan  = float(input("Tunjangan transportasi : "))
potongan   = float(input("Potongan tetap         : "))

# Process
gaji_kotor  = gaji_pokok + tunjangan
gaji_bersih = gaji_kotor - potongan

# Output
print("\n--- Slip Gaji ---")
print("Gaji pokok             :", gaji_pokok)
print("Tunjangan transportasi :", tunjangan)
print("Gaji kotor             :", gaji_kotor)
print("Potongan tetap         :", potongan)
print("Gaji bersih            :", gaji_bersih)
