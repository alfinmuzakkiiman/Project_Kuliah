# ========================================================
# A3 - Rincian Belanja Setelah Pajak (Sequence)
# IPO:
# - Input   : nama produk (str), harga satuan (float), jumlah (int)
# - Process : subtotal = harga * jumlah
#             pajak = subtotal * 0.11
#             total = subtotal + pajak
# - Output  : nama produk, subtotal, pajak 11%, total pembayaran
# ========================================================
# Pseudocode:
# MULAI
#   INPUT nama_produk
#   INPUT harga_satuan
#   INPUT jumlah
#   subtotal <- harga_satuan * jumlah
#   pajak <- subtotal * 0.11
#   total <- subtotal + pajak
#   TAMPILKAN nama_produk, subtotal, pajak, total
# SELESAI
# ========================================================

print("=== RINCIAN BELANJA SETELAH PAJAK ===")

# Input
nama_produk  = input("Nama produk   : ")
harga_satuan = float(input("Harga satuan  : "))
jumlah       = int(input("Jumlah beli   : "))

# Process
subtotal = harga_satuan * jumlah
pajak    = subtotal * 0.11
total    = subtotal + pajak

# Output
print("\n--- Struk Belanja ---")
print("Produk          :", nama_produk)
print("Harga satuan    :", harga_satuan)
print("Jumlah          :", jumlah)
print("Subtotal        :", subtotal)
print("Pajak (11%)     :", pajak)
print("Total bayar     :", total)
