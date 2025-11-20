import os

def header():
    os.system("cls")
    print("MENGUKUR LUAS ATAU KELILING PERSEGI PANJANG".center(100, "="))

def input_user():
    panjang = int(input("Masukkan panjang: "))
    lebar = int(input("Masukkan lebar: "))
    return panjang, lebar

def area(panjang, lebar):
    return panjang * lebar

def circumference(panjang, lebar):
    return 2 * (panjang + lebar)

number_of_activities = int(input("Mau melakukan berapa kali perhitugan: "))
i = 0

header()
while i < number_of_activities:
    area_or_circumference = input("Mau menghitung luas/keliling: ").lower()

    if area_or_circumference == "luas":
        panjang_input, lebar_input = input_user()
        luas = area(panjang_input, lebar_input)
        print(f"Luas = {luas}")
        i += 1

    elif area_or_circumference == "keliling":
        panjang_input, lebar_input = input_user()
        keliling = circumference(panjang_input, lebar_input)
        print(f"Keliling = {keliling}")
        i += 1

print("SEMOGA HARIMU MENYENANGKANa".center(100, "="))