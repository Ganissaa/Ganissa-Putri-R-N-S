# list kosong untuk menampung hasil pangkat tiga
kubik = []

for angka in range(1, 15):
    nilai_kubik = angka ** 3  
    kubik.append(nilai_kubik)

for hasil in kubik:
    print(hasil)