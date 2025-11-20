# 0 < i < 5 or 8 < i < 11

angka = float(input("Masukkan angka yang berada di antara 0 sampai 5\ndan berada di antara 8 sampai 11: "))

# 0 < i < 5
komparasi_satu = angka > 0
komparasi_dua = angka < 5
gabungan_satu = komparasi_satu and komparasi_dua
print(f"Apakah angkamu nilainya di antara 0 sampai 5: {gabungan_satu}")

# 8 < i < 11
komparasi_tiga = angka > 8
komparasi_empat = angka < 11
gabungan_dua = komparasi_tiga and komparasi_empat
print(f"Apakah angkamu nilainya di antara 8 sampai 11: {gabungan_dua}")

# 0 < i < 5 or 8 < i < 11
gabungan_tiga = gabungan_satu or gabungan_dua
print(f"Apakah nilai angkamu di antara 0 sampai 5 atau di antara 8 sampai 11: {gabungan_tiga}")