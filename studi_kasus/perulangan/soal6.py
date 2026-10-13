# ========================================================
# Studi Kasus 6 - Perulangan / Iteration
# Kasus: Menghitung Total Penjualan dari 10 Transaksi
# IPO (Input - Process - Output):
# - Input   : Nominal penjualan untuk masing-masing transaksi (1 s/d 10)
# - Process : Akumulasi nilai penjualan ke variabel total_penjualan
# - Output  : Total keseluruhan nominal transaksi
# ========================================================

print("=== SISTEM PENCATATAN 10 TRANSAKSI PENJUALAN ===")

JUMLAH_TRANSAKSI = 10
total_penjualan = 0.0

# Process Input dan Akumulasi
for i in range(1, JUMLAH_TRANSAKSI + 1):
    nilai_transaksi = float(input(f"Masukkan nominal transaksi ke-{i}: Rp "))
    total_penjualan += nilai_transaksi

# Output
print("\n--- REKAP PENJUALAN TOKO ---")
print(f"Jumlah Transaksi Selesai : {JUMLAH_TRANSAKSI}")
print(f"Total Penjualan          : Rp {total_penjualan:,.2f}")
