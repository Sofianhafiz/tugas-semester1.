class Pegawai:
    def __init__(self, nama, status, gaji_pokok, durasi_lembur=0):
        self.nama = nama
        self.status = status  # 'tetap' atau 'tidak tetap'
        self.gaji_pokok = gaji_pokok
        self.durasi_lembur = durasi_lembur

    def hitung_tunjangan(self):
        if self.status == 'tetap':
            return 0.7 * self.gaji_pokok  # Tunjangan 70% dari gaji pokok
        return 0
    
    def hitung_uang_lembur(self):
        persen_lembur = 0.1  # 10% dari gaji pokok
        uang_lembur = self.durasi_lembur * (persen_lembur * self.gaji_pokok)
        return uang_lembur

    def hitung_gaji_bersih(self):
        tunjangan = self.hitung_tunjangan()
        uang_lembur = self.hitung_uang_lembur()
        if self.status == 'tetap':
            return self.gaji_pokok + tunjangan + uang_lembur
        else:
            return self.gaji_pokok + uang_lembur

    def tampilkan_info(self):
        tunjangan = self.hitung_tunjangan()
        uang_lembur = self.hitung_uang_lembur()
        gaji_bersih = self.hitung_gaji_bersih()
        print(f"Nama: {self.nama}")
        print(f"Gaji Pokok: Rp {self.gaji_pokok}")
        print(f"Tunjangan: Rp {tunjangan if self.status == 'tetap' else 0}")
        print(f"Durasi Lembur: {self.durasi_lembur} jam")
        print(f"Uang Lembur: Rp {uang_lembur}")
        print(f"Gaji Bersih: Rp {gaji_bersih}")
        print("-" * 30)

# Membuat objek perusahaan
perusahaan = []

# Menambahkan pegawai tetap dan tidak tetap
perusahaan.append(Pegawai("Ali", "tetap", 5000000, 10))  # Pegawai tetap dengan durasi lembur 10 jam
perusahaan.append(Pegawai("Budi", "tidak tetap", 4000000, 8))  # Pegawai tidak tetap dengan durasi lembur 8 jam
perusahaan.append(Pegawai("Citra", "tetap", 6000000, 5))  # Pegawai tetap dengan durasi lembur 5 jam
perusahaan.append(Pegawai("Dina", "tidak tetap", 3500000, 6))  # Pegawai tidak tetap dengan durasi lembur 6 jam

# Menampilkan informasi gaji pegawai
for pegawai in perusahaan:
    pegawai.tampilkan_info()
