print("Pembuatan Ketupat".center(40, "="))

baris = int(input("Mau berapa baris: "))
if baris % 2 == 0:
    baris += 1

for i in range(baris):
    if i <= baris // 2:
        stars = 2 * i + 1

    else:
        stars = 2 * (baris - i - 1) + 1

    space = (baris - stars) // 2

    print(" " * space + "*" * stars)