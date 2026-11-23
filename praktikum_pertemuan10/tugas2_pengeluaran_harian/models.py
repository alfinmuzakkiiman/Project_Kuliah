# models.py
# Mengelola perhitungan total dan rata-rata pengeluaran harian.


def hitung_total(data_pengeluaran):
    """Menghitung total seluruh pengeluaran harian menggunakan akumulator."""
    total = 0

    for pengeluaran in data_pengeluaran:
        total += pengeluaran

    return total


def hitung_rata_rata(data_pengeluaran):
    """Menghitung rata-rata pengeluaran per hari dari list data pengeluaran."""
    if len(data_pengeluaran) == 0:
        return 0

    total = hitung_total(data_pengeluaran)
    return total / len(data_pengeluaran)
