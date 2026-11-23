# views.py
# Mengelola input dan output aplikasi pengeluaran harian.


def input_jumlah_hari():
    """Meminta input jumlah hari pencatatan pengeluaran dari pengguna."""
    return input("Masukkan Jumlah Hari Pencatatan: ")


def input_pengeluaran(hari):
    """Meminta input nominal pengeluaran hari ke-hari dari pengguna."""
    return input(f"Masukkan Pengeluaran Hari ke-{hari}: Rp ")


def tampilkan_hasil(data_pengeluaran, total_pengeluaran, rata_rata):
    """Menampilkan daftar pengeluaran harian, total, dan rata-rata per hari."""
    print("\n========== REKAP PENGELUARAN HARIAN ==========")

    for i, pengeluaran in enumerate(data_pengeluaran, start=1):
        print(f"Hari ke-{i}: Rp {pengeluaran:,.2f}")

    print("----------------------------------------------")
    print(f"Jumlah Hari Pencatatan : {len(data_pengeluaran)} hari")
    print(f"Total Pengeluaran      : Rp {total_pengeluaran:,.2f}")
    print(f"Rata-rata per Hari     : Rp {rata_rata:,.2f}")
    print("==============================================")


def tampilkan_pesan(pesan):
    """Menampilkan pesan informasi atau kesalahan kepada pengguna."""
    print(pesan)
