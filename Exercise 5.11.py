# Angka 1 sampai 9
angka_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for angka in angka_angka:
    if angka == 1:
        print(f"{angka}st")
    elif angka == 2:
        print(f"{angka}nd")
    elif angka == 3:
        print(f"{angka}rd")
    else:
        print(f"{angka}th")