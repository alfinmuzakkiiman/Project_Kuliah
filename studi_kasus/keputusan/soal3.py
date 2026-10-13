# ========================================================
# Studi Kasus 3 - Keputusan / Decision
# Kasus: Menghitung Biaya Tarif Parkir
# Kondisi:
# - 1 jam pertama                : Rp5.000
# - Setiap jam berikutnya (> 1)  : Tambahan Rp3.000 / jam
# ========================================================

import math

print("=== SISTEM TARIF PARKIR KENDARAAN ===")

# Input
lama_parkir = float(input("Masukkan Lama Parkir (dalam jam): "))

# Process & Decision
# Pembulatan ke atas jika ada kelebihan menit (misal 1.5 jam dihitung 2 jam)
jam_dihitung = math.ceil(lama_parkir)

if jam_dihitung <= 0:
    biaya = 0
    keterangan = "Durasi tidak valid atau 0 jam"
elif jam_dihitung == 1:
    biaya = 5000
    keterangan = "Tarif 1 jam pertama (Rp5.000)"
else:
    biaya = 5000 + (jam_dihitung - 1) * 3000
    keterangan = f"Tarif 1 jam pertama (Rp5.000) + {jam_dihitung - 1} jam tambahan (@Rp3.000)"

# Output
print("\n--- STRUK PARKIR ---")
print("Durasi Input  :", lama_parkir, "jam")
print("Jam Terhitung :", jam_dihitung, "jam")
print("Keterangan    :", keterangan)
print("Total Biaya   : Rp", biaya)
