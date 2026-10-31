# ========================================================
# Studi Kasus Terpadu 1 - Sistem Kasir Mini Market
# Menggabungkan: Sequence, Selection, Looping
# ========================================================
# IPO:
# - Input   : jumlah jenis barang, nama/harga/jumlah tiap barang,
#             status member (member/non-member)
# - Process : validasi input, loop setiap barang, hitung subtotal,
#             akumulasi total, hitung diskon 10% jika >= 500.000,
#             potongan member 20.000 jika member DAN total setelah
#             diskon >= 300.000, total akhir minimal 0
# - Output  : rincian total, diskon, potongan, total akhir
# ========================================================
# Pseudocode:
# MULAI
#   INPUT jumlah_jenis
#   JIKA jumlah_jenis <= 0
#     TAMPILKAN "Jumlah harus > 0"
#     BERHENTI
#   total_belanja <- 0
#   ULANGI sebanyak jumlah_jenis
#     INPUT nama_barang, harga, jumlah
#     Validasi harga > 0 dan jumlah > 0
#     subtotal <- harga * jumlah
#     total_belanja <- total_belanja + subtotal
#   INPUT status_member (normalkan dengan strip().lower())
#   JIKA total_belanja >= 500000
#     diskon_utama <- total_belanja * 0.10
#   SELAIN ITU
#     diskon_utama <- 0
#   total_setelah_diskon <- total_belanja - diskon_utama
#   JIKA status == "member" DAN total_setelah_diskon >= 300000
#     potongan_member <- 20000
#   SELAIN ITU
#     potongan_member <- 0
#   total_akhir <- max(0, total_setelah_diskon - potongan_member)
#   TAMPILKAN rincian
# SELESAI
# ========================================================

print("=== SISTEM KASIR MINI MARKET ===")

# Input jumlah jenis barang
try:
    jumlah_jenis = int(input("Jumlah jenis barang: "))
except ValueError:
    print("Input harus berupa angka!")
    exit()

if jumlah_jenis <= 0:
    print("Jumlah jenis barang harus lebih dari 0!")
    exit()

# Looping input setiap barang
total_belanja = 0

for i in range(1, jumlah_jenis + 1):
    print("\n--- Barang ke-" + str(i) + " ---")
    nama_barang = input("Nama barang  : ")

    # Validasi harga
    while True:
        try:
            harga = float(input("Harga satuan : "))
            if harga <= 0:
                print("Harga harus lebih dari 0! Masukkan ulang.")
            else:
                break
        except ValueError:
            print("Input harus berupa angka! Masukkan ulang.")

    # Validasi jumlah
    while True:
        try:
            jumlah = int(input("Jumlah beli  : "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0! Masukkan ulang.")
            else:
                break
        except ValueError:
            print("Input harus berupa angka! Masukkan ulang.")

    subtotal = harga * jumlah
    total_belanja += subtotal
    print("Subtotal     :", subtotal)

# Input status member
while True:
    status_member = input("\nStatus pelanggan (member/non-member): ").strip().lower()
    if status_member in ["member", "non-member"]:
        break
    else:
        print("Status harus 'member' atau 'non-member'! Masukkan ulang.")

# Hitung diskon utama (Selection)
if total_belanja >= 500000:
    diskon_utama = total_belanja * 0.10
else:
    diskon_utama = 0

total_setelah_diskon = total_belanja - diskon_utama

# Hitung potongan member (Selection)
if status_member == "member" and total_setelah_diskon >= 300000:
    potongan_member = 20000
else:
    potongan_member = 0

# Hitung total akhir (minimal 0)
total_akhir = max(0, total_setelah_diskon - potongan_member)

# Output
print("\n" + "=" * 40)
print("         STRUK BELANJA")
print("=" * 40)
print("Total belanja      : Rp", total_belanja)
print("Diskon utama (10%) : Rp", diskon_utama)
print("Potongan member    : Rp", potongan_member)
print("Total akhir        : Rp", total_akhir)
print("=" * 40)
