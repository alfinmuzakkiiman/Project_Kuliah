# controllers.py
# Mengatur alur proses dan validasi data transaksi penjualan.

import models
import views


def proses_transaksi():
    """Menjalankan proses input, validasi, penyimpanan list, dan perhitungan transaksi."""
    try:
        jumlah = int(views.input_jumlah())

        if jumlah <= 0:
            views.tampilkan_pesan(
                "Jumlah transaksi harus lebih besar dari nol."
            )
            return

    except ValueError:
        views.tampilkan_pesan(
            "Jumlah transaksi harus berupa angka bulat."
        )
        return

    data_transaksi = []

    for i in range(jumlah):
        try:
            nominal = float(views.input_transaksi(i + 1))

            if nominal <= 0:
                views.tampilkan_pesan(
                    "Nominal transaksi harus lebih besar dari nol."
                )
                return

            data_transaksi.append(nominal)

        except ValueError:
            views.tampilkan_pesan(
                "Input nominal transaksi harus berupa angka."
            )
            return

    total_pendapatan = models.hitung_total(data_transaksi)
    rata_rata = models.hitung_rata_rata(data_transaksi)

    views.tampilkan_hasil(data_transaksi, total_pendapatan, rata_rata)
