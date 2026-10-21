# ========================================================
# Praktikum 5 - Operator Aritmatika
# Kasus: Menghitung Nilai Akhir
# IPO:
# - Input   : nilai tugas, UTS, UAS (float, rentang 0-100)
# - Process : nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)
# - Output  : nilai akhir berbobot
# ========================================================
# Bobot: Tugas = 30%, UTS = 30%, UAS = 40%

print("=== MENGHITUNG NILAI AKHIR ===")

# Input
tugas = float(input("Nilai tugas (0-100): "))
uts   = float(input("Nilai UTS   (0-100): "))
uas   = float(input("Nilai UAS   (0-100): "))

# Process
nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)

# Output
print("\nNilai akhir:", nilai_akhir)
