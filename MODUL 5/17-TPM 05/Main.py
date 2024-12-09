# Input status member
is_member = input("Apakah Member? (ya/tidak): ").strip().lower()

# Input total belanja
total_belanja = float(input("Input total belanja (Rp): "))

# Menentukan diskon
if is_member == "ya":  # Jika pelanggan adalah member
    if total_belanja > 500000:
        diskon_persen = 20  # Diskon 20%
    else:
        diskon_persen = 10  # Diskon 10%
else:  # Jika pelanggan bukan member
    if total_belanja > 500000:
        diskon_persen = 5  # Diskon 5%
    else:
        diskon_persen = 0  # Tidak ada diskon

# Menghitung diskon dan total bayar
diskon_rp = total_belanja * diskon_persen / 100
total_bayar = total_belanja - diskon_rp

# Menampilkan hasil
print(f"\nTotal belanja : Rp {total_belanja:,.0f}")
print(f"Diskon persen : {diskon_persen}%")
print(f"Diskon        : Rp {diskon_rp:,.0f}")
print(f"Bayar         : Rp {total_bayar:,.0f}")