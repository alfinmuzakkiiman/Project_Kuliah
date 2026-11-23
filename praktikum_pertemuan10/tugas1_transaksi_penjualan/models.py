# models.py
# Mengelola perhitungan total pendapatan dan rata-rata transaksi penjualan.


def hitung_total(data_transaksi):
    """Menghitung total seluruh nominal transaksi menggunakan akumulator."""
    total = 0

    for nominal in data_transaksi:
        total += nominal

    return total


def hitung_rata_rata(data_transaksi):
    """Menghitung rata-rata nominal transaksi dari list data transaksi."""
    if len(data_transaksi) == 0:
        return 0

    total = hitung_total(data_transaksi)
    return total / len(data_transaksi)
