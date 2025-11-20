data_thoriq = {
    "Nama" : "Muhammad Thoriq Sadewo",
    "NIM" : 25031554079,
    "Asal" : "Jakarta"
}

data_gilang = {
    "Nama" : "Gilang Hidayat",
    "NIM" : 25031554169,
    "Asal" : "Jakarta"
}

data_iqbal = {
    "Nama" : "Muhammad Iqbal Zaki",
    "NIM" : 25031554269,
    "Asal" : "Lumajang"
}

data_gabungan = {
    "SADA079" : data_thoriq,
    "SADA169" : data_gilang,
    "SADA269" : data_iqbal
}

print("\n","DATA MAHASISWA KELAS C".center(70, "="), "\n")
print(f"{"KODE":^9}{"NAMA":^50}{"NIM":^13}{"ASAL":^10}")
print("="*80)

for i in data_gabungan: 
    nama = data_gabungan[i]["Nama"]
    nim = data_gabungan[i]["NIM"]
    asal = data_gabungan[i]["Asal"]
    print(f"{i:^9}{nama:^50}{nim:^13}{asal:^10}")