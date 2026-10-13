# ========================================================
# Studi Kasus 2 - Keputusan / Decision
# Kasus: Menghitung Diskon Belanja Toko (10% jika >= Rp100.000)
# Kondisi:
# - Jika total belanja >= 100.000 -> diskon 10%
# - Jika total belanja < 100.000  -> diskon 0%
# ========================================================

print("=== SISTEM PERHITUNGAN DISKON TOKO ===")

# Input
total_belanja = float(input("Masukkan Total Belanja: Rp "))

# Process & Decision
if total_belanja >= 100000:
    diskon = total_belanja * 0.10
    status_diskon = "Mendapat Diskon 10%"
else:
    diskon = 0.0
    status_diskon = "Tidak Mendapat Diskon"

total_bayar = total_belanja - diskon

# Output
print("\n--- RINCIAN PEMBAYARAN ---")
print("Total Belanja : Rp", total_belanja)
print("Status Promo  :", status_diskon)
print("Potongan      : Rp", diskon)
print("Total Bayar   : Rp", total_bayar)
