# ========================================================
# Latihan Mandiri 4 - Tipe Data dan Variabel
# Tugas: Apa perbedaan nilai 25 dengan "25"?
#        Berikan satu contoh operasi yang menunjukkan perbedaannya.
# ========================================================

print("=== PERBEDAAN int 25 DAN str '25' ===")

angka_int = 25    # integer -> bilangan bulat untuk operasi aritmetika
angka_str = "25"  # string  -> teks, diperlakukan sebagai karakter

print("\nNilai angka_int :", angka_int, "| Tipe:", type(angka_int).__name__)
print("Nilai angka_str :", angka_str, "| Tipe:", type(angka_str).__name__)

# Contoh perbedaan nyata menggunakan operator +
print("\n--- Contoh Operasi dengan + ---")
print("int  : 25 + 10      =", angka_int + 10)       # penjumlahan aritmetika -> 35
print("str  : '25' + '10'  =", angka_str + "10")     # penggabungan teks (concatenation) -> '2510'

# Kesimpulan
print("\nKesimpulan:")
print("- int  25  digunakan untuk PERHITUNGAN (operasi aritmetika)")
print("- str '25' digunakan sebagai TEKS / IDENTITAS (bukan angka)")
