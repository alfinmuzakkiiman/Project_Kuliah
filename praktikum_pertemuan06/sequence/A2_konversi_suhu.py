# ========================================================
# A2 - Konversi Suhu (Sequence)
# IPO:
# - Input   : suhu dalam Celsius (float)
# - Process : Fahrenheit = (Celsius * 9/5) + 32
#             Kelvin = Celsius + 273.15
# - Output  : suhu dalam Celsius, Fahrenheit, dan Kelvin
# ========================================================
# Pseudocode:
# MULAI
#   INPUT celsius
#   fahrenheit <- (celsius * 9/5) + 32
#   kelvin <- celsius + 273.15
#   TAMPILKAN celsius, fahrenheit, kelvin
# SELESAI
# ========================================================

print("=== KONVERSI SUHU ===")

# Input
celsius = float(input("Masukkan suhu dalam Celsius: "))

# Process
fahrenheit = (celsius * 9/5) + 32
kelvin     = celsius + 273.15

# Output
print("\n--- Hasil Konversi ---")
print("Celsius    :", celsius, "°C")
print("Fahrenheit :", fahrenheit, "°F")
print("Kelvin     :", kelvin, "K")
