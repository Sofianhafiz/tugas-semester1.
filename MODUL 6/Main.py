# Daftar pegawai dan statusnya
pegawai = [
    {"nama": "Andi", "status": "tetap", "gaji_pokok": 5000000, "durasi_lembur": 5},
    {"nama": "Budi", "status": "tidak tetap", "gaji_pokok": 4000000, "durasi_lembur": 3},
    {"nama": "Cici", "status": "tetap", "gaji_pokok": 6000000, "durasi_lembur": 2},
    {"nama": "Deni", "status": "tidak tetap", "gaji_pokok": 4500000, "durasi_lembur": 4},
    {"nama": "Eka", "status": "tetap", "gaji_pokok": 7000000, "durasi_lembur": 1},
    # Tambahkan data pegawai lainnya sesuai kebutuhan
]

# Fungsi untuk menghitung gaji bersih
def hitung_gaji(pegawai):
    if pegawai["status"] == "tetap":
        tunjangan = 0.7 * pegawai["gaji_pokok"]  # Tunjangan 70% dari gaji pokok
        lembur = pegawai["durasi_lembur"] * (0.1 * pegawai["gaji_pokok"])  # Lembur 10% per jam dari gaji pokok
        gaji_bersih = pegawai["gaji_pokok"] + tunjangan + lembur
        return gaji_bersih, tunjangan
    elif pegawai["status"] == "tidak tetap":
        lembur = pegawai["durasi_lembur"] * pegawai["gaji_pokok"]  # Lembur = durasi lembur * gaji pokok
        gaji_bersih = pegawai["gaji_pokok"] + lembur
        return gaji_bersih, 0  # Tidak ada tunjangan untuk pegawai tidak tetap

# Menampilkan informasi pegawai
for p in pegawai:
    gaji_bersih, tunjangan = hitung_gaji(p)
    print(f"Nama: {p['nama']}")
    print(f"Gaji Pokok: {p['gaji_pokok']}")
    if tunjangan > 0:
        print(f"Tunjangan: {tunjangan}")
    print(f"Durasi Lembur: {p['durasi_lembur']} jam")
    print(f"Gaji Bersih: {gaji_bersih}\n")
