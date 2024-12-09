# percabangan 
# percabangan 1 kondisi

# struktur percabangan
"""
  1.if-nya
  2.kondisinya, steatment yang harus terpenuhi agar aksi di jalankan 
  3.aksinya
"""


nama = input("masukan nama anda")

# percabangan 
# if <kondisi> : <aksi>
if nama == "adam" : print("selamat datang")
print("terima kasih") # bukan aksi

# percabangan dengan identitas 
if nama == "adam":
    print("selamat datang") # aksi
    print("selamat belajar") # aksi
print("terima kasih") # bukan aksi

# percabangan dengan Else statement
if nama == "adam":
    print("selamat datang") 
else:
    print("Anda Bukan Adam")

print("program berakhir")