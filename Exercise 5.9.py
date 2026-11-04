daftar_pengguna = ['admin', 'yaya', 'lala', 'adel', 'amel']

# Pemeriksa apakah daftar tidak kosong
if daftar_pengguna:
    for pengguna in daftar_pengguna:
        if pengguna == 'admin':
            print(" Halo admin, apakah Anda ingin melihat laporan status?")
        else:
            print(f" Halo {pengguna}, terima kasih sudah masuk kembali.")
else:
    print("Kita perlu mencari beberapa pengguna!")

# Mengosongkan daftar untuk menguji apakah pesan kosong
daftar_pengguna = []

if daftar_pengguna:
    for pengguna in daftar_pengguna:
        print(f"Halo {pengguna}")
else:
    print(" Kita perlu mencari beberapa pengguna!")