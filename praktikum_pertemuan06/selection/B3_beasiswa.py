# ========================================================
# B3 - Kelayakan Beasiswa (Selection)
# IPO:
# - Input   : IPK (float), status mahasiswa (str: aktif/tidak aktif)
# - Process : validasi IPK 0-4
#             jika IPK >= 3.50 DAN status == "aktif" -> memenuhi syarat
#             selain itu -> belum memenuhi syarat
# - Output  : pesan kelayakan beasiswa
# ========================================================
# Pseudocode:
# MULAI
#   INPUT ipk
#   INPUT status
#   Normalkan status dengan strip().lower()
#   JIKA ipk < 0 ATAU ipk > 4
#     TAMPILKAN "IPK tidak valid"
#   SELAIN ITU
#     JIKA ipk >= 3.50 DAN status == "aktif"
#       TAMPILKAN "Memenuhi syarat beasiswa"
#     SELAIN ITU
#       TAMPILKAN "Belum memenuhi syarat beasiswa"
# SELESAI
# ========================================================

print("=== KELAYAKAN BEASISWA ===")

# Input
ipk    = float(input("Masukkan IPK (0-4)          : "))
status = input("Status mahasiswa (aktif/tidak aktif): ").strip().lower()

# Process & Output
if ipk < 0 or ipk > 4:
    print("\nIPK tidak valid! IPK harus antara 0 - 4.")
else:
    print("\nIPK    :", ipk)
    print("Status :", status)

    if ipk >= 3.50 and status == "aktif":
        print("Hasil  : Memenuhi syarat beasiswa")
    else:
        print("Hasil  : Belum memenuhi syarat beasiswa")
