# ========================================================
# Studi Kasus 5 - Keputusan / Decision
# Kasus: Penentuan Denda Keterlambatan Pengembalian Buku Perpustakaan
# Kondisi:
# - Keterlambatan > 7 hari       : Denda Rp20.000
# - Keterlambatan 1 - 7 hari     : Denda Rp5.000
# - Tidak terlambat (<= 0 hari)  : Denda Rp0
# ========================================================

print("=== SISTEM DENDA PERPUSTAKAAN ===")

# Input
keterlambatan = int(input("Masukkan Keterlambatan Pengembalian (hari): "))

# Process & Decision
if keterlambatan <= 0:
    denda = 0
    status = "Tepat Waktu (Tidak Kena Denda)"
elif keterlambatan > 7:
    denda = 20000
    status = "Terlambat Berat (> 7 hari)"
else:
    denda = 5000
    status = "Terlambat Ringan (1 - 7 hari)"

# Output
print("\n--- STATUS PENGEMBALIAN BUKU ---")
print("Keterlambatan :", keterlambatan, "hari")
print("Kategori      :", status)
print("Total Denda   : Rp", denda)
