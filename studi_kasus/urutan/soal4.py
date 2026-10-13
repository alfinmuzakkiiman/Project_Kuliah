# ========================================================
# Studi Kasus 4 - Runtunan / Sequence
# Kasus: Menghitung Nilai Akhir Mahasiswa (Bobot 20%, 30%, 50%)
# IPO (Input - Process - Output):
# - Input   : nilai tugas, nilai UTS, nilai UAS (float)
# - Process : nilai_akhir = (tugas * 0.20) + (uts * 0.30) + (uas * 0.50)
# - Output  : nilai akhir mahasiswa
# ========================================================

print("=== PERHITUNGAN NILAI AKHIR ===")

# Input
tugas = float(input("Masukkan nilai Tugas (20%): "))
uts = float(input("Masukkan nilai UTS   (30%): "))
uas = float(input("Masukkan nilai UAS   (50%): "))

# Process
nilai_akhir = (tugas * 0.20) + (uts * 0.30) + (uas * 0.50)

# Output
print("\n--- HASIL AKHIR ---")
print("Nilai Tugas :", tugas)
print("Nilai UTS   :", uts)
print("Nilai UAS   :", uas)
print("Nilai Akhir =", nilai_akhir)
