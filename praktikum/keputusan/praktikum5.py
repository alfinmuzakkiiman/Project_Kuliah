print("=== GRADE MAHASISWA ===")

nilai = float(input("Nilai: "))

if nilai >= 85:
    grade = "A"
elif nilai >= 75:
    grade = "B"
elif nilai >= 65:
    grade = "C"
elif nilai >= 50:
    grade = "D"
else:
    grade = "E"

print("Grade =", grade)