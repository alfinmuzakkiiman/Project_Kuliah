# controllers.py
# Mengatur alur proses dan validasi data pengeluaran harian.

import models
import views


def proses_pengeluaran():
    """Menjalankan proses input, validasi, penyimpanan list, dan perhitungan pengeluaran."""
    try:
        jumlah_hari = int(views.input_jumlah_hari())

        if jumlah_hari <= 0:
            views.tampilkan_pesan(
                "Jumlah hari pencatatan harus lebih besar dari nol."
            )
            return

    except ValueError:
        views.tampilkan_pesan(
            "Jumlah hari pencatatan harus berupa angka bulat."
        )
        return

    data_pengeluaran = []

    for i in range(jumlah_hari):
        try:
            pengeluaran = float(views.input_pengeluaran(i + 1))

            if pengeluaran < 0:
                views.tampilkan_pesan(
                    "Nominal pengeluaran tidak boleh negatif."
                )
                return

            data_pengeluaran.append(pengeluaran)

        except ValueError:
            views.tampilkan_pesan(
                "Input nominal pengeluaran harus berupa angka."
            )
            return

    total_pengeluaran = models.hitung_total(data_pengeluaran)
    rata_rata = models.hitung_rata_rata(data_pengeluaran)

    views.tampilkan_hasil(data_pengeluaran, total_pengeluaran, rata_rata)
