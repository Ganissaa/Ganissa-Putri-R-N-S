# Meminta pengguna memasukkan nama mereka
nama = input("Masukkan nama Anda: ")

# Menentukan nama file tujuan
nama_file = 'tamu.txt'

# Membuka file dalam mode tulis ('w') dan menyimpan nama ke dalamnya
with open(nama_file, 'w') as file_obj:
    file_obj.write(nama)

print(f"Terima kasih! Nama '{nama}' telah disimpan ke dalam file {nama_file}.")