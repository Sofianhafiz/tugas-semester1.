# Input nilai
nilai = float(input("Masukkan nilai: "))

# Menentukan grade berdasarkan nilai
if nilai > 90:
    grade = "A"
elif nilai > 80 and nilai <= 90:
    grade = "A-"
elif nilai > 74 and nilai <= 80:
    grade = "B+"
elif nilai > 69 and nilai <= 74:
    grade = "B"
elif nilai > 64 and nilai <= 69:
    grade = "C+"
elif nilai > 59 and nilai <= 64:
    grade = "C"
elif nilai > 54 and nilai <= 59:
    grade = "D"
else:
    grade = "E"

# Menampilkan hasil
print(f"Nilai: {nilai}, Grade: {grade}")