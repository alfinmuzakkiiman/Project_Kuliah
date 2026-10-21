# ========================================================
# Latihan Mandiri 4 - Operator Aritmatika
# Tugas: Menghitung total belanja dari harga satuan dan jumlah barang.
#        Tampilkan total sebelum dan setelah diskon 10%.
# IPO:
# - Input   : harga satuan (float), jumlah barang (int)
# - Process : total = harga * jumlah
#             diskon = total * 0.10
#             total_setelah_diskon = total - diskon
# - Output  : total sebelum diskon, potongan diskon, total setelah diskon
# ========================================================

print("=== TOTAL BELANJA DENGAN DISKON ===")

# Input
harga  = float(input("Harga satuan  : "))
jumlah = int(input("Jumlah barang : "))

# Process
total                = harga * jumlah
diskon               = total * 0.10
total_setelah_diskon = total - diskon

# Output
print("\n--- Struk Belanja ---")
print("Total sebelum diskon :", total)
print("Diskon 10%           :", diskon)
print("Total setelah diskon :", total_setelah_diskon)
