# ========================================================
# Studi Kasus 6 - Runtunan / Sequence
# Kasus: Menghitung Total Pembayaran Toko Online (Termasuk Ongkir)
# IPO (Input - Process - Output):
# - Input   : harga barang (float), jumlah barang (int), biaya pengiriman (float)
# - Process : subtotal = harga_barang * jumlah_barang
#             total_bayar = subtotal + biaya_pengiriman
# - Output  : subtotal barang, ongkir, dan total yang harus dibayar
# ========================================================

print("=== TRANSAKSI PEMBELIAN TOKO ONLINE ===")

# Input
harga_barang = float(input("Masukkan Harga Barang   : Rp "))
jumlah_barang = int(input("Masukkan Jumlah Barang  : "))
biaya_pengiriman = float(input("Masukkan Ongkos Kirim   : Rp "))

# Process
subtotal = harga_barang * jumlah_barang
total_bayar = subtotal + biaya_pengiriman

# Output
print("\n--- RINGKASAN PEMBAYARAN ---")
print("Subtotal Barang   : Rp", subtotal)
print("Biaya Pengiriman  : Rp", biaya_pengiriman)
print("---------------------------------------")
print("Total Pembayaran  : Rp", total_bayar)
