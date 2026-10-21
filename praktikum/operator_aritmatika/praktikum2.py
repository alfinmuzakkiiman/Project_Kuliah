# ========================================================
# Praktikum 2 - Operator Aritmatika
# Kasus: Membagi Barang Sama Rata
# IPO:
# - Input   : jumlah barang (int), jumlah orang (int)
# - Process : per_orang = jumlah_barang // jumlah_orang
#             sisa = jumlah_barang % jumlah_orang
# - Output  : barang per orang dan sisa barang
# ========================================================
# Catatan: Operator // (pembagian bulat) menghasilkan bilangan
# bulat hasil bagi, sedangkan % (modulus) menghasilkan sisa bagi.

print("=== MEMBAGI BARANG SAMA RATA ===")

# Input
jumlah_barang = int(input("Jumlah barang: "))
jumlah_orang  = int(input("Jumlah orang : "))

# Process & Output
if jumlah_orang > 0:
    per_orang = jumlah_barang // jumlah_orang
    sisa = jumlah_barang % jumlah_orang
    print("\nBarang per orang:", per_orang)
    print("Sisa barang     :", sisa)
else:
    print("Jumlah orang harus lebih dari nol.")
