# ========================================================
# C3 - Menu Transaksi Berulang (Looping)
# IPO:
# - Input   : pilihan menu (1/2/3), dimensi sesuai pilihan
# - Process : pilihan 1 -> luas persegi panjang = panjang * lebar
#             pilihan 2 -> luas segitiga = 0.5 * alas * tinggi
#             pilihan 3 -> keluar (break)
#             lainnya   -> pesan tidak valid
# - Output  : hasil luas atau pesan keluar
# ========================================================
# Pseudocode:
# MULAI
#   SELAMA True
#     TAMPILKAN menu
#     INPUT pilihan
#     JIKA pilihan = "1"
#       INPUT panjang, lebar
#       luas <- panjang * lebar
#       TAMPILKAN luas
#     JIKA pilihan = "2"
#       INPUT alas, tinggi
#       luas <- 0.5 * alas * tinggi
#       TAMPILKAN luas
#     JIKA pilihan = "3"
#       TAMPILKAN "Terima kasih"
#       BERHENTI
#     SELAIN ITU
#       TAMPILKAN "Pilihan tidak valid"
# SELESAI
# ========================================================

print("=== MENU TRANSAKSI PERHITUNGAN ===")

while True:
    print("\n--- Menu ---")
    print("1. Hitung Luas Persegi Panjang")
    print("2. Hitung Luas Segitiga")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        panjang = float(input("Masukkan panjang: "))
        lebar   = float(input("Masukkan lebar  : "))
        luas    = panjang * lebar
        print("Luas persegi panjang:", luas)

    elif pilihan == "2":
        alas   = float(input("Masukkan alas  : "))
        tinggi = float(input("Masukkan tinggi: "))
        luas   = 0.5 * alas * tinggi
        print("Luas segitiga:", luas)

    elif pilihan == "3":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")
