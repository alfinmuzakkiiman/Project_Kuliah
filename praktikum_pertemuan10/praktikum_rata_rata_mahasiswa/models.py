# models.py
# Mengelola proses perhitungan rata-rata.


def hitung_rata_rata(data_nilai):
    total = 0

    for nilai in data_nilai:
        total += nilai

    return total / len(data_nilai)
