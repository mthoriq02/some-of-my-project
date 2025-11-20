print("Kalkulator untuk menghitung 2 angka".center(50, "="))

angka_pertama = float(input("Masukkan angka pertama anda: "))
angka_kedua = float(input("Masukkan angka kedua anda: "))
operator = input("Masukkan jenis operator (-, +, *, /): ")

if operator == "-":
    hasil = angka_pertama - angka_kedua
    print(f"Hasilnya adalah: {hasil}")

elif operator == "*":
    hasil = angka_pertama * angka_kedua
    print(f"Hasilnya adalah: {hasil}")

elif operator == "+":
    hasil = angka_pertama + angka_kedua
    print(f"Hasilnya adalah: {hasil}")

elif operator == "/":
    hasil = angka_pertama / angka_kedua
    print(f"Hasilnya adalah: {hasil}")

else:
    print("Operator tidak valid!")

print("Semoga harimu menyenangkan!")