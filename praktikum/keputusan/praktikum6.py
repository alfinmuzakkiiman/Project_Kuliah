print("=== DISKON BELANJA ===")

total = float(input("Total belanja: "))

if total >= 100000:
    diskon = total * 0.10
else:
    diskon = 0

bayar = total - diskon

print("Diskon =", diskon)
print("Total bayar =", bayar)