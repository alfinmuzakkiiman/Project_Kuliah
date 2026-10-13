# ========================================================
# Praktikum 1 - Tipe Data dan Variabel
# Kasus: Profil Mahasiswa
# IPO:
# - Input   : Data mahasiswa (didefinisikan langsung sebagai variabel)
# - Process : Simpan data pada variabel dengan tipe data yang sesuai
# - Output  : Tampilkan semua data mahasiswa
# ========================================================
# Catatan: NIM disimpan sebagai string (str) karena NIM merupakan
# kode identitas, bukan nilai yang digunakan untuk operasi aritmetika.

print("=== PROFIL MAHASISWA ===")

# Variabel data mahasiswa
nama  = "Alfin Muzakki Iman"  # str   -> teks/nama
nim   = "261106050033"         # str   -> identitas, bukan angka
umur  = 20                    # int   -> bilangan bulat
ipk   = 3.85                  # float -> bilangan desimal
aktif = True                  # bool  -> status logika (aktif/tidak)

# Output
print("Nama           :", nama)
print("NIM            :", nim)
print("Umur           :", umur, "tahun")
print("IPK            :", ipk)
print("Mahasiswa Aktif:", aktif)
