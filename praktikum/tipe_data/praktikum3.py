# ========================================================
# Praktikum 3 - Tipe Data dan Variabel
# Kasus: Total Belanja
# IPO:
# - Input   : harga satuan (float), jumlah barang (int)
# - Process : total = harga * jumlah
# - Output  : total pembayaran
# ========================================================

print("=== TOTAL BELANJA ===")

# Input
harga  = float(input("Harga satuan  : "))
jumlah = int(input("Jumlah barang : "))

# Process
total = harga * jumlah

# Output
print("\nHarga satuan    :", harga)
print("Jumlah          :", jumlah)
print("Total pembayaran:", total)
