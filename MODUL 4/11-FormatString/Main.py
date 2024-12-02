# format string
# katakunci f 

# contoh generic 
# string 
nama  = "Amad Dialo"
format_str = f"Hallo {nama}"
print(format_str)
print("Hallo", nama)

# boolean 
boolean = False
formaat_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5 
formaat_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
formaat_str = f"bilangan bulat = {angka :d}"
print(format_str)

# bilangan dengan ordo ribuan 
angka = 2000000
formaat_str = f"jutaan = {angka :,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
formaat_str = f"desimal = {angka :.3f}"
print(format_str)

# menampilkan tanda + dam -
angka_minus = -10
angka_plus = +10.1234
formaat_minus = f"minus = {angka_minus :+d}"
formaat_plus = f"plus = {angka_plus :2f}"

print(formaat_minus)
print(formaat_plus)

# format persen
presaentasi = 0.045 #
formaat_persen = f"persen = {presaentasi :.2%}"
print(formaat_persen)
