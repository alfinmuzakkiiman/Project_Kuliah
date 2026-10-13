# ========================================================
# Latihan Mandiri 6 - Tipe Data dan Variabel
# Tugas: Sistem akademik menyimpan NIM, nama, IPK, jumlah SKS,
#        dan status aktif. Tentukan tipe data masing-masing beserta alasannya.
# ========================================================

print("=== SISTEM DATA AKADEMIK MAHASISWA ===")

# Definisi variabel beserta alasan pemilihan tipe data
nim          = "261106050033"       # str   -> identitas unik, tidak pernah dihitung
nama         = "Alfin Muzakki Iman" # str   -> teks nama orang
ipk          = 3.85                 # float -> nilai desimal (rentang 0.00 - 4.00)
jumlah_sks   = 120                  # int   -> SKS selalu bilangan bulat
status_aktif = True                 # bool  -> hanya dua nilai: aktif (True) / tidak (False)

# Output data beserta tipe
print("\n--- Data Mahasiswa ---")
print("NIM          :", nim,          "| Tipe:", type(nim).__name__)
print("Nama         :", nama,         "| Tipe:", type(nama).__name__)
print("IPK          :", ipk,          "| Tipe:", type(ipk).__name__)
print("Jumlah SKS   :", jumlah_sks,   "| Tipe:", type(jumlah_sks).__name__)
print("Status Aktif :", status_aktif, "| Tipe:", type(status_aktif).__name__)

# Penjelasan alasan pemilihan tipe data
print("\n--- Alasan Pemilihan Tipe Data ---")
print("NIM          : str   -> kode identitas, tidak digunakan untuk operasi aritmetika")
print("Nama         : str   -> berupa teks nama orang")
print("IPK          : float -> memiliki nilai desimal (contoh: 3.75, 3.85)")
print("Jumlah SKS   : int   -> selalu bilangan bulat, tidak ada nilai 0.5 SKS")
print("Status Aktif : bool  -> hanya dua kemungkinan: True (aktif) atau False (tidak)")
