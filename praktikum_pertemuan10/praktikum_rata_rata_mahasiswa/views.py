# views.py
# Mengelola input dan output program.


def input_jumlah():
    return input("Masukkan Jumlah Mahasiswa: ")


def input_nilai(nomor):
    return input(f"Masukkan Nilai Mahasiswa ke-{nomor}: ")


def tampilkan_hasil(data_nilai, hasil):
    print("\n========== HASIL PERHITUNGAN ==========")

    for i, nilai in enumerate(data_nilai, start=1):
        print(f"Nilai Mahasiswa ke-{i}: {nilai:g}")

    print("---------------------------------------")
    print(f"Rata-rata Nilai: {hasil:.2f}")
    print("=======================================")


def tampilkan_pesan(pesan):
    print(pesan)
