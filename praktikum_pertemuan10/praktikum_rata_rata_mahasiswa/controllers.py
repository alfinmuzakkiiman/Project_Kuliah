# controllers.py
# Mengatur proses dan validasi perhitungan.

import models
import views


def proses_perhitungan():

    try:
        jumlah = int(views.input_jumlah())

        if jumlah <= 0:
            views.tampilkan_pesan(
                "Jumlah mahasiswa harus lebih besar dari nol."
            )
            return

    except ValueError:
        views.tampilkan_pesan(
            "Jumlah mahasiswa harus berupa angka bulat."
        )
        return

    data_nilai = []

    for i in range(jumlah):

        try:
            nilai = float(views.input_nilai(i + 1))

            if nilai < 0 or nilai > 100:
                views.tampilkan_pesan(
                    "Nilai harus berada antara 0 sampai 100."
                )
                return

            data_nilai.append(nilai)

        except ValueError:
            views.tampilkan_pesan(
                "Input nilai harus berupa angka."
            )
            return

    hasil = models.hitung_rata_rata(data_nilai)

    views.tampilkan_hasil(data_nilai, hasil)
