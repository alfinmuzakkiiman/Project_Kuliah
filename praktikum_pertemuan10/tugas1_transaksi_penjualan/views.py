# views.py
# Mengelola input dan output aplikasi transaksi penjualan.


def input_jumlah():
    """Meminta input jumlah transaksi penjualan dari pengguna."""
    return input("Masukkan Jumlah Transaksi: ")


def input_transaksi(nomor):
    """Meminta input nominal transaksi ke-nomor dari pengguna."""
    return input(f"Masukkan Nominal Transaksi ke-{nomor}: Rp ")


def tampilkan_hasil(data_transaksi, total_pendapatan, rata_rata):
    """Menampilkan daftar transaksi, total pendapatan, dan rata-rata."""
    print("\n========== REKAP TRANSAKSI PENJUALAN ==========")

    for i, nominal in enumerate(data_transaksi, start=1):
        print(f"Transaksi ke-{i}: Rp {nominal:,.2f}")

    print("-----------------------------------------------")
    print(f"Jumlah Transaksi    : {len(data_transaksi)}")
    print(f"Total Pendapatan    : Rp {total_pendapatan:,.2f}")
    print(f"Rata-rata Transaksi : Rp {rata_rata:,.2f}")
    print("===============================================")


def tampilkan_pesan(pesan):
    """Menampilkan pesan informasi atau kesalahan kepada pengguna."""
    print(pesan)
