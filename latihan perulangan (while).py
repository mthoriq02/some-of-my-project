print(f"Pembuatan Ketupat".center(40, "="))

count = 1
sisi = int(input("Mau berapa sisi: "))
if sisi % 2 == 0:
    sisi += 1
space = int((sisi / 2))

while count <= sisi:
    if count % 2:
        print(" " * space, "*" * count)
        count += 1
        space -= 1

    else:
        count += 1
        continue

space = 1
sisi = sisi - 1

while sisi != 0:
    if sisi % 2:
        print(" " * space, "*" * sisi)
        sisi -= 1
        space += 1

    else:
        sisi -= 1
        continue