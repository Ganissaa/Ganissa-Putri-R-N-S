#1 Kesamaan dan ketidaksamaan string
mobil = "subaru"

print("Tes 1: Apakah mobil adalah subaru?")
print(mobil == "subaru") 

print("Apakah mobil adalah honda?")
print(mobil == "honda")  

#2 Menggunakan lower()
nama = "Amel"

print("\nTes 2: Apakah nama setelah huruf kecil adalah amel?")
print(nama.lower() == "amel")  

print("Apakah nama setelah huruf kecil adalah ameLs?")
print(nama.lower() == "ameL")  

#3 Anggka menggunakan perbandingan
umur = 25

print("\nTes 3: Apakah umur lebih besar dari 17?")
print(umur > 17)  

print("Apakah umur lebih kecil dari 20?")
print(umur < 20)  

#4 Menggunakan and dan or
nilai = 90

print("\nTes 4: Apakah nilai lebih dari 80 dan kurang dari 100?")
print(nilai > 80 and nilai < 100) 

print("Apakah nilai kurang dari 50 atau lebih dari 100?")
print(nilai < 50 or nilai > 100)  

#5 Apakah item ada di dalam list
buah = ["apel", "mangga", "Nanas"]

print("\nTes 5: Apakah apel ada di dalam daftar buah?")
print("apel" in buah) 

print("Apakah pisang ada di dalam daftar buah?")
print("pisang" in buah) 

#6 Apakah item tidak ada di dalam list
print("\nTes 6: Apakah pisang tidak ada di dalam daftar buah?")
print("pisang" not in buah)

print("Apakah apel tidak ada di dalam daftar buah?")
print("apel" not in buah) 
