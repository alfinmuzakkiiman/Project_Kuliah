# Tugas Kuliah: Dasar Pemrograman Python

Repositori ini berisi kumpulan tugas praktikum dan studi kasus mata kuliah **Dasar Pemrograman (Algoritma dan Pemrograman)** menggunakan bahasa pemrograman **Python 3**.

Project ini mencakup 3 pilar utama struktur dasar algoritma pemrograman:
1. **Runtunan / Urutan (Sequence)**
2. **Keputusan / Percabangan (Decision / Branching)**
3. **Pengulangan (Iteration / Looping)**

---

## Struktur Direktori

```text
Tugas/
├── praktikum/                       # Latihan modul praktikum dasar
│   ├── Runtunan/
│   │   ├── praktikum1.py            # Menghitung Luas dan Keliling Persegi Panjang
│   │   ├── praktikum2.py            # Menghitung Total Belanja Sederhana
│   │   └── praktikum3.py            # Menghitung Nilai Akhir Mahasiswa
│   ├── keputusan/
│   │   ├── praktikum4.py            # Menentukan Status Kelulusan (if-else)
│   │   ├── praktikum5.py            # Menentukan Grade Mahasiswa (if-elif-else)
│   │   └── praktikum6.py            # Menghitung Diskon Belanja (if-else)
│   ├── Pengulangan/
│   │   ├── praktikum7.py            # Menampilkan Angka 1 s/d 5 (for loop)
│   │   ├── praktikum8.py            # Menghitung Penjumlahan Angka 1 s/d 10
│   │   └── praktikum9.py            # Menampilkan Bilangan Genap (range step)
│   └── tipe_data/
│       ├── praktikum1.py            # Profil Mahasiswa (Mendefinisikan Variabel)
│       ├── praktikum2.py            # Input dan Konversi Tipe Data
│       ├── praktikum3.py            # Total Belanja (float & int)
│       ├── praktikum4.py            # Menggabungkan Teks (String Concatenation)
│       └── praktikum5.py            # Mengatasi Kesalahan Tipe Data (TypeError)
│
├── studi_kasus/                     # Pemecahan masalah studi kasus lengkap (IPO terstruktur)
│   ├── urutan/                      # Studi Kasus - Runtunan / Sequence (6 Soal)
│   │   ├── soal1.py                 # Luas Permukaan & Volume Balok
│   │   ├── soal2.py                 # Kasir Kantin (Nasi Goreng & Es Teh)
│   │   ├── soal3.py                 # Konversi Suhu Celsius ke Fahrenheit & Kelvin
│   │   ├── soal4.py                 # Perhitungan Nilai Akhir Mahasiswa (20%, 30%, 50%)
│   │   ├── soal5.py                 # Slip Gaji Bersih Karyawan
│   │   └── soal6.py                 # Transaksi Toko Online (Termasuk Ongkos Kirim)
│   ├── keputusan/                   # Studi Kasus - Decision / Percabangan (6 Soal)
│   │   ├── soal1.py                 # Penentuan Kelulusan (Batas Nilai >= 60)
│   │   ├── soal2.py                 # Diskon Toko 10% (Belanja >= Rp100.000)
│   │   ├── soal3.py                 # Sistem Tarif Parkir Kendaraan (Bertingkat & Pembulatan)
│   │   ├── soal4.py                 # Penentuan Grade Nilai Mahasiswa (A, B, C, D, E)
│   │   ├── soal5.py                 # Sistem Denda Keterlambatan Buku Perpustakaan
│   │   └── soal6.py                 # Sistem Autentikasi Login (Operator Logika AND)
│   └── perulangan/                  # Studi Kasus - Iteration / Perulangan (6 Soal)
│       ├── soal1.py                 # Menampilkan Angka 1 Sampai 10
│       ├── soal2.py                 # Menghitung Akumulasi Deret Angka 1 Sampai 100
│       ├── soal3.py                 # Menampilkan Bilangan Genap 2 Sampai 20
│       ├── soal4.py                 # Input & Pengolahan Rata-Rata Nilai 5 Mahasiswa
│       ├── soal5.py                 # Tabel Perkalian Angka 7 (1 s/d 10)
│       └── soal6.py                 # Akumulasi 10 Transaksi Penjualan Toko
│
└── latihan_mandiri/                 # Latihan mandiri per pertemuan
    └── tipe_data/                   # Pertemuan 04 - Tipe Data dan Variabel (6 Latihan)
        ├── latihan1.py              # Empat Variabel Barang dengan Tipe Data Tepat
        ├── latihan2.py              # Luas Persegi Panjang (float)
        ├── latihan3.py              # Dua Angka dan Empat Operasi Aritmetika
        ├── latihan4.py              # Perbedaan int 25 dan str '25'
        ├── latihan5.py              # Perbaikan Kode TypeError (angka + 5)
        └── latihan6.py              # Sistem Data Akademik Mahasiswa + Alasan Tipe Data
```

---

## Ringkasan Studi Kasus

Setiap file di dalam folder `studi_kasus/` dirancang dengan pendekatan **IPO (Input - Process - Output)** yang rapi dan mudah dipahami:

### 1. Urutan / Sequence (`studi_kasus/urutan/`)
* **soal1.py**: Menerima input panjang, lebar, dan tinggi balok, lalu menghitung luas permukaan ($2 \times (pl + pt + lt)$) dan volume ($p \times l \times t$).
* **soal2.py**: Simulasi kasir kantin untuk menghitung total pembelian Nasi Goreng (Rp15.000) dan Es Teh (Rp5.000).
* **soal3.py**: Konversi suhu dari Celsius ke Fahrenheit ($(\frac{9}{5} \times C) + 32$) dan Kelvin ($C + 273.15$).
* **soal4.py**: Menghitung nilai akhir berbobot dari Tugas (20%), UTS (30%), dan UAS (50%).
* **soal5.py**: Menghitung gaji bersih karyawan (`gaji_pokok + tunjangan - potongan`).
* **soal6.py**: Menghitung total belanja toko online dari harga, kuantitas barang, dan ongkir tanpa percabangan.

### 2. Keputusan / Decision (`studi_kasus/keputusan/`)
* **soal1.py**: Menentukan kelulusan mahasiswa: LULUS jika nilai $\ge 60$, selain itu TIDAK LULUS.
* **soal2.py**: Memberikan diskon 10% jika total belanja mencapai minimal Rp100.000.
* **soal3.py**: Tarif parkir: 1 jam pertama Rp5.000, jam berikutnya dikenakan tambahan Rp3.000/jam (menggunakan `math.ceil`).
* **soal4.py**: Menentukan grade nilai: `A` ($\ge 85$), `B` ($\ge 75$), `C` ($\ge 65$), `D` ($\ge 50$), dan `E` ($< 50$).
* **soal5.py**: Denda perpustakaan: $> 7$ hari denda Rp20.000, $1-7$ hari denda Rp5.000, tepat waktu Rp0.
* **soal6.py**: Sistem login dengan operator logika `and` untuk memvalidasi kesesuaian username dan password.

### 3. Perulangan / Iteration (`studi_kasus/perulangan/`)
* **soal1.py**: Menampilkan deret bilangan 1 sampai 10 menggunakan `for` dan `range(1, 11)`.
* **soal2.py**: Menghitung akumulasi penjumlahan angka 1 s/d 100 dengan variabel penampung total.
* **soal3.py**: Menampilkan bilangan genap antara 2 sampai 20 menggunakan langkah step `range(2, 21, 2)`.
* **soal4.py**: Meminta input nilai untuk 5 mahasiswa secara berulang, lalu menampilkan daftar nilai, total, dan rata-rata kelas.
* **soal5.py**: Menampilkan tabel perkalian angka 7 (dari $7 \times 1$ hingga $7 \times 10$) secara terformat rapi.
* **soal6.py**: Mengakumulasi nominal penjualan dari 10 transaksi berturut-turut.

---

## Cara Menjalankan Program

### Prasyarat
- Pastikan **Python 3** sudah terinstal pada komputer Anda. Periksa versi dengan perintah:
  ```bash
  python3 --version
  ```

### Menjalankan Program
Buka terminal dan arahkan ke direktori project, lalu jalankan script yang diinginkan:

```bash
# Contoh menjalankan studi kasus urutan
python3 studi_kasus/urutan/soal1.py

# Contoh menjalankan studi kasus keputusan
python3 studi_kasus/keputusan/soal1.py

# Contoh menjalankan studi kasus perulangan
python3 studi_kasus/perulangan/soal4.py

# Contoh menjalankan praktikum
python3 praktikum/Runtunan/praktikum1.py
```

---

## Catatan Pemrograman
- Seluruh kode ditulis secara modular dan self-explanatory dengan komentar berbahasa Indonesia.
- Menggunakan fungsi bawaan standar Python tanpa memerlukan instalasi library pihak ketiga (*zero external dependencies*).
