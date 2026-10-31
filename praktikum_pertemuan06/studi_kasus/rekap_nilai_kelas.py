# ========================================================
# Studi Kasus Terpadu 2 - Sistem Rekap Nilai Kelas
# Menggabungkan: Sequence, Selection, Looping
# ========================================================
# IPO:
# - Input   : jumlah mahasiswa N, nama/tugas/UTS/UAS tiap mahasiswa
# - Process : validasi N > 0, validasi nilai 0-100
#             nilai_akhir = 0.30*tugas + 0.30*UTS + 0.40*UAS
#             predikat: A>=85, B>=75, C>=65, D>=50, E<50
#             status: lulus jika nilai_akhir >= 60
#             akumulasi total_nilai, jumlah_lulus, jumlah_tidak_lulus
#             rata_rata_kelas = total_nilai / N
# - Output  : hasil individu per mahasiswa, rekap kelas
# ========================================================
# Pseudocode:
# MULAI
#   INPUT N
#   JIKA N <= 0
#     TAMPILKAN "Jumlah mahasiswa harus > 0"
#     BERHENTI
#   total_nilai <- 0
#   jumlah_lulus <- 0
#   jumlah_tidak_lulus <- 0
#   ULANGI i dari 1 sampai N
#     INPUT nama, tugas, uts, uas
#     Validasi tugas, uts, uas dalam rentang 0-100
#     nilai_akhir <- 0.30*tugas + 0.30*uts + 0.40*uas
#     Tentukan predikat (A/B/C/D/E)
#     JIKA nilai_akhir >= 60: status <- "Lulus"
#     SELAIN ITU: status <- "Tidak Lulus"
#     TAMPILKAN nama, nilai_akhir, predikat, status
#     total_nilai <- total_nilai + nilai_akhir
#     Perbarui jumlah_lulus atau jumlah_tidak_lulus
#   rata_rata_kelas <- total_nilai / N
#   TAMPILKAN rekap kelas
# SELESAI
# ========================================================

print("=== SISTEM REKAP NILAI KELAS ===")

# Input jumlah mahasiswa
try:
    n = int(input("Jumlah mahasiswa: "))
except ValueError:
    print("Input harus berupa angka!")
    exit()

if n <= 0:
    print("Jumlah mahasiswa harus lebih dari nol!")
    exit()

# Inisialisasi akumulator
total_nilai        = 0
jumlah_lulus       = 0
jumlah_tidak_lulus = 0

# Looping input dan proses setiap mahasiswa
for i in range(1, n + 1):
    print("\n--- Mahasiswa ke-" + str(i) + " ---")
    nama = input("Nama  : ")

    # Validasi nilai tugas
    while True:
        try:
            tugas = float(input("Tugas : "))
            if tugas < 0 or tugas > 100:
                print("Nilai harus 0-100! Masukkan ulang.")
            else:
                break
        except ValueError:
            print("Input harus berupa angka! Masukkan ulang.")

    # Validasi nilai UTS
    while True:
        try:
            uts = float(input("UTS   : "))
            if uts < 0 or uts > 100:
                print("Nilai harus 0-100! Masukkan ulang.")
            else:
                break
        except ValueError:
            print("Input harus berupa angka! Masukkan ulang.")

    # Validasi nilai UAS
    while True:
        try:
            uas = float(input("UAS   : "))
            if uas < 0 or uas > 100:
                print("Nilai harus 0-100! Masukkan ulang.")
            else:
                break
        except ValueError:
            print("Input harus berupa angka! Masukkan ulang.")

    # Hitung nilai akhir (Sequence)
    nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)

    # Tentukan predikat (Selection)
    if nilai_akhir >= 85:
        predikat = "A"
    elif nilai_akhir >= 75:
        predikat = "B"
    elif nilai_akhir >= 65:
        predikat = "C"
    elif nilai_akhir >= 50:
        predikat = "D"
    else:
        predikat = "E"

    # Tentukan status lulus (Selection - terpisah dari predikat)
    if nilai_akhir >= 60:
        status_lulus = "Lulus"
        jumlah_lulus += 1
    else:
        status_lulus = "Tidak Lulus"
        jumlah_tidak_lulus += 1

    # Tampilkan hasil individu
    print("Nilai Akhir :", nilai_akhir)
    print("Predikat    :", predikat)
    print("Status      :", status_lulus)

    # Akumulasi
    total_nilai += nilai_akhir

# Hitung rata-rata kelas (Sequence)
rata_rata_kelas = total_nilai / n

# Output rekap kelas
print("\n" + "=" * 40)
print("        REKAP NILAI KELAS")
print("=" * 40)
print("Jumlah mahasiswa      :", n)
print("Jumlah lulus          :", jumlah_lulus)
print("Jumlah tidak lulus    :", jumlah_tidak_lulus)
print("Rata-rata nilai kelas :", rata_rata_kelas)
print("=" * 40)
