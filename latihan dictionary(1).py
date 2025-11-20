import datetime as dt
import os
import random
import string

print("SELAMAT DATANG DI PUSAT DATA MAHASISWA".center(100, "="))
template = {
    "Nama": "",
    "NIM": 0000,
    "Asal": "",
    "Tanggal Lahir": 00-00-0000
}
mahasiswa = {}
jumlah_data = int(input("Mau memasukkan berapa data: "))
a = 0

while a < jumlah_data:
    os.system("cls")
    data_mahasiswa = dict.fromkeys(template.keys())
    data_mahasiswa["Nama"] = input("Nama: ")
    data_mahasiswa["NIM"] = int(input("NIM: "))
    data_mahasiswa["Asal"] = input("Asal: ")
    tanggal_lahir = int(input("Tanggal Lahir: "))
    bulan_lahir = int(input("Bulan lahir: "))
    tahun_lahir = int(input("Tahun Lahir: "))
    kelahiran = dt.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)
    data_mahasiswa["Tanggal Lahir"] = kelahiran.strftime("%d-%m-%Y")
    a += 1
    kode = "".join(random.choice(string.ascii_uppercase) for i in range(6))
    mahasiswa.update({kode:data_mahasiswa})
    os.system("cls")

    print(f"\n{"KEY":^6}{"NAMA":^50}{"NIM":^13}{"ASAL":^15}{"TANGGAL LAHIR":^12}")
    print("=" * 97)

    for j in mahasiswa:
        data = j

        nama = mahasiswa[j]["Nama"]
        nim = mahasiswa[j]["NIM"]
        asal = mahasiswa[j]["Asal"]
        lahir = mahasiswa[j]["Tanggal Lahir"]

        print(f"{j:^6}{nama:^50}{nim:^13}{asal:^15}{lahir:^12}")