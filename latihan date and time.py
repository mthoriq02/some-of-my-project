import datetime as dt

print("SELAMAT DATANG DI PENGECEKAN UMUR".center(40, "="))

tahun = int(input(f"Tahun lahir: "))
bulan = int(input(f"Bulan lahir: "))
tanggal = int(input(f"Tanggal lahir: "))
kelahiran = dt.date(tahun, bulan, tanggal)
hari = f"Hari lahir: {kelahiran:%A}"

print(kelahiran)
print(hari)

hari_ini = dt.date.today()
umur_dalam_hari = hari_ini - kelahiran
umur = f"{umur_dalam_hari.days // 365} tahun {(umur_dalam_hari.days % 365) // 30} bulan {(umur_dalam_hari.days % 30)} hari"

print(umur)