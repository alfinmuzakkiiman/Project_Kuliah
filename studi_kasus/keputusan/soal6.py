# ========================================================
# Studi Kasus 6 - Keputusan / Decision
# Kasus: Sistem Autentikasi Login (Username & Password)
# Kondisi yang diperiksa:
# - Menggunakan operator logika 'and': kedua nilai (username dan password)
#   harus cocok dengan data kredensial yang valid secara bersamaan.
# - Jika cocok  -> 'Login berhasil'
# - Jika salah  -> 'Login gagal'
# ========================================================

print("=== SISTEM LOGIN PENGGUNA ===")

# Kredensial akun yang terdaftar
USERNAME_VALID = "admin"
PASSWORD_VALID = "admin123"

# Input
username_input = input("Masukkan Username : ")
password_input = input("Masukkan Password : ")

# Process & Decision
if username_input == USERNAME_VALID and password_input == PASSWORD_VALID:
    status_login = "Login berhasil"
    pesan = "Selamat datang kembali ke sistem!"
else:
    status_login = "Login gagal"
    pesan = "Username atau password yang Anda masukkan salah."

# Output
print("\n--- STATUS AUTENTIKASI ---")
print("Status :", status_login)
print("Pesan  :", pesan)
