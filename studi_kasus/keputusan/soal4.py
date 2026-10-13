# ========================================================
# Studi Kasus 4 - Keputusan / Decision
# Kasus: Penentuan Grade Nilai Mahasiswa
# Aturan Keputusan:
# - Nilai >= 85 : Grade A
# - Nilai >= 75 : Grade B
# - Nilai >= 65 : Grade C
# - Nilai >= 50 : Grade D
# - Nilai < 50  : Grade E
# ========================================================

print("=== SISTEM PENENTUAN GRADE NILAI ===")

# Input
nilai = float(input("Masukkan Nilai Mahasiswa (0 - 100): "))

# Process & Decision
if nilai >= 85:
    grade = "A"
    keterangan = "Sangat Memuaskan"
elif nilai >= 75:
    grade = "B"
    keterangan = "Memuaskan"
elif nilai >= 65:
    grade = "C"
    keterangan = "Cukup"
elif nilai >= 50:
    grade = "D"
    keterangan = "Kurang"
else:
    grade = "E"
    keterangan = "Sangat Kurang (Gagal)"

# Output
print("\n--- HASIL PENILAIAN ---")
print("Nilai      :", nilai)
print("Grade      :", grade)
print("Keterangan :", keterangan)
