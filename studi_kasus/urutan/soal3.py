# ========================================================
# Studi Kasus 3 - Runtunan / Sequence
# Kasus: Konversi Suhu Celsius ke Fahrenheit dan Kelvin
# IPO (Input - Process - Output):
# - Input   : suhu dalam Celsius (float)
# - Process : Fahrenheit = (9 / 5 * Celsius) + 32
#             Kelvin     = Celsius + 273.15
# - Output  : suhu dalam derajat Fahrenheit dan Kelvin
# ========================================================

print("=== KONVERSI SUHU CELSIUS ===")

# Input
celsius = float(input("Masukkan suhu dalam Celsius: "))

# Process
fahrenheit = (9 / 5 * celsius) + 32
kelvin = celsius + 273.15

# Output
print("\n--- HASIL KONVERSI ---")
print("Suhu Celsius    =", celsius, "derajat C")
print("Suhu Fahrenheit =", fahrenheit, "derajat F")
print("Suhu Kelvin     =", kelvin, "K")
