# import fungsi date

import datetime as dt

tanggal = 2
bulan = 12
tahun = 2005

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(tanggal_lahir)
hari_ini = dt.date.today()
print(hari_ini)

usia = hari_ini - tanggal_lahir
print(usia)

# hitung usia dalam tahun dan bulan 

usia_tahun = hari_ini.year - tanggal_lahir.year
usia_bulan = hari_ini.month - tanggal_lahir.month

# cetak usia
print(f"usia : {usia_tahun} tahun, {usia_bulan} bulan")