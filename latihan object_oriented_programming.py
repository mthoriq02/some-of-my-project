import os

class calculator:
    def __init__(self):
        self.hasil = 0
        self.angka1 = 0
        self.angka2 = 0
        self.operator = ""

    def add(self):
        self.hasil += (self.angka1 + self.angka2)
    
    def minus(self):
        self.hasil += (self.angka1 - self.angka2)
    
    def multiplied(self):
        self.hasil += (self.angka1 * self.angka2)
    
    def divided (self):
        try:
            if self.angka2 != 0:
                self.hasil += (self.angka1 / self.angka2)

            elif self.angka2 == 0:
                raise ZeroDivisionError

        except ZeroDivisionError:
            print("Pembagian tidak valid!")
    
    def main(self):
        os.system("cls")
        print("SELAMAT DATANG DI KALKULATOR SEDERHANA".center(60, "="))

        number_of_operation = int(input("Masukkan jumlah operasi yang mau dilakukan: "))
        i = 0
        while i < number_of_operation:
            self.angka1 = float(input("Masukkan angka pertama: "))
            self.angka2 = float(input("Masukkan angka kedua: "))
            self.operator = input("Masukkan operator matematika (+, -, *, /): ")
            
            if self.operator == "+":
                self.add()
                i += 1
            elif self.operator == "-":
                self.minus()
                i += 1
            elif self.operator == "*":
                self.multiplied()
                i += 1
            elif self.operator == "/":
                self.divided()
                i += 1

            print(self.hasil)

if __name__ == "__main__":
    try:
        start = calculator()
        start.main()

    except KeyboardInterrupt:
        print("Kode dihentikan manual menggunakan CTRL +C")