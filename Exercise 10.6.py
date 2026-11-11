print(" Program Penjumlahan Dua Angka ")

try:
    angka_pertama = input("Masukkan angka pertama: ")
    angka_pertama = float(angka_pertama)
    
    angka_kedua = input("Masukkan angka kedua: ")
    angka_kedua = float(angka_kedua)
    
except ValueError:
    print("Error: Mohon masukkan angka yang valid, bukan teks atau huruf!")
else:
    hasil = angka_pertama + angka_kedua
    print(f"Hasil penjumlahan: {hasil}")