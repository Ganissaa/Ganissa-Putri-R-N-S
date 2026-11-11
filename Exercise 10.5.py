# Menentukan nama file untuk buku tamu
nama_file = 'para_tamu.txt'

print(" Buku Tamu ")
print("Ketik 'keluar' jika sudah selesai memasukkan nama.\n")

# Membuka file dalam mode tulis ('w')
with open(nama_file, 'w') as file_obj:
    while True:
        nama = input("Masukkan nama Anda: ")
        
        # Kondisi untuk menghentikan perulangan jika pengguna mengetik 'keluar'
        if nama.lower() == 'keluar':
            break
            
        # Menulis nama ke file dengan menambahkan baris baru (\n) di setiap entri
        file_obj.write(f"{nama}\n")
        print(f"Halo {nama}, nama Anda telah ditambahkan ke buku tamu.")

print(f"\nSemua nama tamu berhasil disimpan ke dalam file {nama_file}.")