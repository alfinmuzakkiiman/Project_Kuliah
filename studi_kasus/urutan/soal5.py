# ========================================================
# Studi Kasus 5 - Runtunan / Sequence
# Kasus: Menghitung Gaji Bersih Karyawan
# IPO (Input - Process - Output):
# - Input   : gaji pokok, tunjangan, potongan (float)
# - Process : gaji_bersih = gaji_pokok + tunjangan - potongan
# - Output  : rincian penghasilan dan gaji bersih
# ========================================================

print("=== PERHITUNGAN GAJI BERSIH KARYAWAN ===")

# Input
gaji_pokok = float(input("Masukkan Gaji Pokok : Rp "))
tunjangan = float(input("Masukkan Tunjangan  : Rp "))
potongan = float(input("Masukkan Potongan   : Rp "))

# Process
gaji_bersih = gaji_pokok + tunjangan - potongan

# Output
print("\n--- SLIP GAJI ---")
print("Gaji Pokok  : Rp", gaji_pokok)
print("Tunjangan   : Rp", tunjangan)
print("Potongan    : Rp", potongan)
print("---------------------------------")
print("Gaji Bersih : Rp", gaji_bersih)
