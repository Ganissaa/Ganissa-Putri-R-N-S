def baca_file_silent(nama_file):
    "Membaca file dan mengabaikan error secara senyap jika file tidak ada."
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            isi = file.read()
            print(f" Isi dari {nama_file} ")
            print(isi.strip())
    except FileNotFoundError:
        pass  # Perintah pass membuat program tidak mencetak apa pun saat terjadi FileNotFoundError

daftar_file = ['cat.txt', 'dog.txt', 'birds.txt']

for nama_file in daftar_file:
    baca_file_silent(nama_file)
    print()