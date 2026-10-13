# ========================================================
# Studi Kasus 1 - Keputusan / Decision
# Kasus: Menentukan Status Kelulusan Mahasiswa
# Kondisi:
# - Jika nilai >= 60 -> LULUS
# - Selain itu        -> TIDAK LULUS
# ========================================================

print("=== SISTEM PENENTUAN KELULUSAN ===")

# Input
nilai = float(input("Masukkan Nilai Mahasiswa (0 - 100): "))

# Process & Decision
if nilai >= 60:
    status = "LULUS"
    keterangan = "Selamat, Anda dinyatakan lulus!"
else:
    status = "TIDAK LULUS"
    keterangan = "Mohon maaf, Anda harus mengulang."

# Output
print("\n--- HASIL KELULUSAN ---")
print("Nilai  :", nilai)
print("Status :", status)
print("Pesan  :", keterangan)
