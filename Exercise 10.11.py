import json

# Meminta angka favorit dari pengguna
angka_favorit = input("Berapa angka favorit Anda? ")

nama_file = 'favorite_number.json'

# Menyimpan angka ke dalam file menggunakan json.dumps()
with open(nama_file, 'w') as file:
    json.dump(angka_favorit, file)
    
print("Angka favorit Anda telah berhasil disimpan!")
