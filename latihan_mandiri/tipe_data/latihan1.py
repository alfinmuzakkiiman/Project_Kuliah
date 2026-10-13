# ========================================================
# Latihan Mandiri 1 - Tipe Data dan Variabel
# Tugas: Buat empat variabel: nama barang, harga, jumlah, dan tersedia.
#        Pilih tipe data yang tepat untuk masing-masing variabel.
# ========================================================

print("=== DATA BARANG ===")

# Definisi variabel dengan tipe data yang tepat
nama_barang = "Pensil 2B"  # str   -> nama adalah teks, bukan angka
harga       = 3500.0       # float -> harga bisa memiliki nilai desimal
jumlah      = 12           # int   -> jumlah selalu bilangan bulat
tersedia    = True         # bool  -> status ketersediaan (ada/tidak ada)

# Output beserta informasi tipe data
print("Nama Barang :", nama_barang, " | Tipe:", type(nama_barang).__name__)
print("Harga       :", harga,       " | Tipe:", type(harga).__name__)
print("Jumlah      :", jumlah,      " | Tipe:", type(jumlah).__name__)
print("Tersedia    :", tersedia,    " | Tipe:", type(tersedia).__name__)
