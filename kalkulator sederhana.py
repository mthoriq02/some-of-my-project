print("=====Konversi Fahrenheit Ke Kelvin dan Kelvin ke Fahrenheit=====")

Fahrenheit = int(input("Masukkan suhu dalam satuan Fahrenheit: "))
celcius = (5/9) * (Fahrenheit - 32)
Kelvin = celcius + 273

print(f"{Kelvin} K")

Kelvin = int(input("Masukkan dalam satuan Kelvin: "))
celcius = Kelvin - 273
Fahrenheit = (9/5) * celcius + 32

print(f"{Fahrenheit} derajat F")