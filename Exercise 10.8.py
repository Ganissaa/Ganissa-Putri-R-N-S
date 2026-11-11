def baca_file_hewan(nama_file):
    "Fungsi untuk mencoba membaca dan mencetak isi file."
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            isi = file.read()
            print(f" Isi dari {nama_file} ")
            print(isi.strip())
    except FileNotFoundError:
        print(f"Maaf, file '{nama_file}' tidak ditemukan.")

# Daftar file yang akan dibaca (termasuk file fiktif untuk menguji error)
daftar_file = ['cat.txt', 'dog.txt', 'bird.txt']

for nama_file in daftar_file:
    baca_file_hewan(nama_file)
    print()