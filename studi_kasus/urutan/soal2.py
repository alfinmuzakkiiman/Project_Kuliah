# ========================================================
# Studi Kasus 2 - Runtunan / Sequence
# Kasus: Menghitung Total Pembelian Kantin
# IPO (Input - Process - Output):
# - Input   : jumlah nasi goreng, jumlah es teh (int)
# - Process : total = (jumlah_nasi_goreng * 15000) + (jumlah_es_teh * 5000)
# - Output  : rincian harga dan total pembelian
# ========================================================

print("=== KASIR KANTIN ===")
print("Harga Menu:")
print("- Nasi Goreng : Rp15.000")
print("- Es Teh      : Rp5.000\n")

# Input
HARGA_NASI_GORENG = 15000
HARGA_ES_TEH = 5000

jumlah_nasi_goreng = int(input("Jumlah Nasi Goreng: "))
jumlah_es_teh = int(input("Jumlah Es Teh: "))

# Process
subtotal_nasi_goreng = jumlah_nasi_goreng * HARGA_NASI_GORENG
subtotal_es_teh = jumlah_es_teh * HARGA_ES_TEH
total_pembelian = subtotal_nasi_goreng + subtotal_es_teh

# Output
print("\n--- STRUK PEMBELIAN ---")
print("Total Nasi Goreng : Rp", subtotal_nasi_goreng)
print("Total Es Teh      : Rp", subtotal_es_teh)
print("Total Pembelian   : Rp", total_pembelian)
