jumlah_data = int(input("Mau masukin berapa data: "))
belanja_harian = []
data = 0

while data < jumlah_data:
    barang = input("Nama barang: ")
    harga = input("Harga barang: ")
    belanjaan = [barang, harga]
    belanja_harian.append(belanjaan)
    data += 1
    print("Daftar Belanjaan".center(40, "="), "\n")
    
    for i,j in enumerate(belanja_harian):
        print(f"{i + 1} | {j[0]} | {j[1]}")

print("SELAMAT BERBELANJA!".center(40, "="))