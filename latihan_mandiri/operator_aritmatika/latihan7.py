# ========================================================
# Latihan Mandiri 7 - Operator Aritmatika
# Tugas: Modifikasi program nilai akhir agar menampilkan
#        selisih antara nilai UAS dan nilai tugas.
# IPO:
# - Input   : nilai tugas, UTS, UAS (float, rentang 0-100)
# - Process : nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)
#             selisih = uas - tugas
# - Output  : nilai akhir berbobot dan selisih UAS - tugas
# ========================================================
# Bobot: Tugas = 30%, UTS = 30%, UAS = 40%

print("=== NILAI AKHIR DAN SELISIH UAS - TUGAS ===")

# Input
tugas = float(input("Nilai tugas (0-100): "))
uts   = float(input("Nilai UTS   (0-100): "))
uas   = float(input("Nilai UAS   (0-100): "))

# Process
nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)
selisih     = uas - tugas

# Output
print("\n--- Hasil ---")
print("Nilai akhir          :", nilai_akhir)
print("Selisih UAS - Tugas  :", selisih)
