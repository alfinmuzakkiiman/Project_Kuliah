# ========================================================
# Studi Kasus 4 - Perulangan / Iteration
# Kasus: Memasukkan dan Memproses Nilai 5 Mahasiswa
# IPO (Input - Process - Output):
# - Input   : Nilai mahasiswa ke-1 sampai ke-5 secara berulang
# - Process : Akumulasi total nilai dan hitung rata-rata
# - Output  : Ringkasan total dan rata-rata nilai kelas
# ========================================================

print("=== INPUT NILAI 5 MAHASISWA ===")

JUMLAH_MAHASISWA = 5
daftar_nilai = []
total_nilai = 0.0

# Process Input berulang
for i in range(1, JUMLAH_MAHASISWA + 1):
    nilai = float(input(f"Masukkan nilai Mahasiswa ke-{i}: "))
    daftar_nilai.append(nilai)
    total_nilai += nilai

# Process Hitung Rata-rata
rata_rata = total_nilai / JUMLAH_MAHASISWA

# Output
print("\n--- REKAP NILAI MAHASISWA ---")
for idx, n in enumerate(daftar_nilai, start=1):
    print(f"Mahasiswa {idx} : {n}")

print("-----------------------------")
print(f"Total Nilai  : {total_nilai}")
print(f"Rata-rata    : {rata_rata:.2f}")
