
# =====================================================
# UTS TAKE HOME - APLIKASI TOKO ATK SEKOLAH
# Menggunakan: Sequence, Selection, dan Looping
# =====================================================

print("=======================================")
print("       SELAMAT DATANG DI TOKO ATK")
print("=======================================")

# MENU UTAMA
while True:
    print("\n============= MENU UTAMA =============")
    print("1. Transaksi Penjualan")
    print("2. Keluar")
    print("=======================================")

    pilihan = input("Masukkan pilihan (1/2): ")

    # =========================================
    # PILIHAN 1 - TRANSAKSI PENJUALAN
    # =========================================
    if pilihan == "1":

        print("\n=== TRANSAKSI PENJUALAN ===")

        # INPUT JUMLAH JENIS BARANG
        while True:
            try:
                jumlah_jenis = int(input("Masukkan jumlah jenis barang: "))

                if jumlah_jenis > 0:
                    break
                else:
                    print("Jumlah jenis barang harus lebih dari 0!")

            except ValueError:
                print("Input harus berupa angka bulat!")

        # INISIALISASI TOTAL BELANJA DAN RINCIAN
        total_belanja = 0
        rincian_barang = ""

        # =====================================
        # LOOPING INPUT SETIAP BARANG
        # =====================================
        for i in range(1, jumlah_jenis + 1):

            print("\n--- Barang ke-", i, "---")

            nama_barang = input("Nama barang: ")

            # VALIDASI HARGA SATUAN
            while True:
                try:
                    harga_satuan = float(input("Harga satuan: Rp"))

                    if harga_satuan > 0:
                        break
                    else:
                        print("Harga harus lebih dari 0!")

                except ValueError:
                    print("Input harga harus berupa angka!")

            # VALIDASI JUMLAH PEMBELIAN
            while True:
                try:
                    jumlah_beli = int(input("Jumlah beli: "))

                    if jumlah_beli > 0:
                        break
                    else:
                        print("Jumlah beli harus lebih dari 0!")

                except ValueError:
                    print("Jumlah beli harus berupa angka bulat!")

            # MENGHITUNG SUBTOTAL
            subtotal = harga_satuan * jumlah_beli

            # MENGAKUMULASI TOTAL BELANJA
            total_belanja += subtotal

            # MENYIMPAN RINCIAN BARANG TANPA LIST/ARRAY
            rincian_barang += (
                "Barang ke-" + str(i) + "\n"
                + "Nama barang   : " + nama_barang + "\n"
                + "Harga satuan  : Rp" + str(harga_satuan) + "\n"
                + "Jumlah beli   : " + str(jumlah_beli) + "\n"
                + "Subtotal      : Rp" + str(subtotal) + "\n\n"
            )

            print("Subtotal:", subtotal)

        # =====================================
        # TOTAL BELANJA
        # =====================================
        print("\nTotal belanja: Rp", total_belanja)

        # =====================================
        # INPUT STATUS MEMBER
        # =====================================
        while True:
            status_member = input(
                "Status pelanggan (member/non-member): "
            ).strip().lower()

            if status_member == "member" or status_member == "non-member":
                break
            else:
                print("Status harus member atau non-member!")

        # =====================================
        # MENGHITUNG DISKON UTAMA
        # =====================================
        diskon_utama = 0

        if total_belanja >= 500000:
            diskon_utama = total_belanja * 0.10

        # TOTAL SETELAH DISKON UTAMA
        total_setelah_diskon = total_belanja - diskon_utama

        # =====================================
        # MENGHITUNG POTONGAN MEMBER
        # =====================================
        potongan_member = 0

        if status_member == "member" and total_setelah_diskon >= 300000:
            potongan_member = 20000

        # =====================================
        # MENGHITUNG TOTAL PEMBAYARAN
        # =====================================
        total_bayar = total_setelah_diskon - potongan_member

        # Memastikan total pembayaran minimal Rp0
        if total_bayar < 0:
            total_bayar = 0

        # =====================================
        # MENAMPILKAN RINCIAN DISKON
        # =====================================
        print("\n========== RINCIAN DISKON ==========")
        print("Total belanja       : Rp", total_belanja)
        print("Diskon utama (10%)  : Rp", diskon_utama)
        print("Potongan member     : Rp", potongan_member)
        print("Total pembayaran    : Rp", total_bayar)
        print("====================================")

        # =====================================
        # INPUT PEMBAYARAN
        # =====================================
        while True:
            try:
                uang_bayar = float(input("\nMasukkan uang pembayaran: Rp"))

                if uang_bayar >= total_bayar:
                    break
                else:
                    kekurangan = total_bayar - uang_bayar
                    print("Pembayaran belum mencukupi!")
                    print("Kekurangan: Rp", kekurangan)

            except ValueError:
                print("Input pembayaran harus berupa angka!")

        # =====================================
        # MENGHITUNG KEMBALIAN
        # =====================================
        kembalian = uang_bayar - total_bayar

        # =====================================
        # MENAMPILKAN STRUK BELANJA
        # =====================================
        print("\n=======================================")
        print("           TOKO ATK SEKOLAH")
        print("              STRUK BELANJA")
        print("=======================================")

        print(rincian_barang)

        print("---------------------------------------")
        print("Total belanja       : Rp", total_belanja)
        print("Diskon utama        : Rp", diskon_utama)
        print("Potongan member     : Rp", potongan_member)
        print("Total pembayaran    : Rp", total_bayar)
        print("Uang pembayaran     : Rp", uang_bayar)
        print("Kembalian           : Rp", kembalian)
        print("=======================================")
        print("       TERIMA KASIH TELAH BERBELANJA")
        print("=======================================")

    # =========================================
    # PILIHAN 2 - KELUAR
    # =========================================
    elif pilihan == "2":

        print("\nTerima kasih telah berbelanja di Toko ATK!")
        print("Program selesai.")
        break

    # =========================================
    # PILIHAN TIDAK VALID
    # =========================================
    else:
        print("\nPilihan tidak valid! Silakan pilih 1 atau 2.")
