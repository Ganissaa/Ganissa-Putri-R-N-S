# Kamus kosong untuk menyimpan data hasil survei
responses = {}

# Variabel aktif untuk mengontrol perulangan
polling_active = True

while polling_active:
    # Meminta nama dan jawaban dari pengguna
    nama = input("\nSiapakah nama kamu? ")
    destinasi = input("Jika kamu bisa mengunjungi satu tempat di dunia, tempat apa yang akan kamu kunjungi? ")
    
    # Menyimpan jawaban
    responses[nama] = destinasi
    
    # Menanyakan apakah ada orang lain yang ingin ikut survei
    ulangi = input("Apakah ada orang lain yang ingin ikut survei? (ya/tidak): ")
    if ulangi.lower() == 'tidak':
        polling_active = False

# Polling selesai, menampilkan hasil survei
print("\nHASIL SURVEI LIBURAN IMPIAN")
for nama, destinasi in responses.items():
    print(f"{nama} ingin sekali berkunjung ke {destinasi}.")