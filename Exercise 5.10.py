# Daftar pengguna yang sudah terdaftar saat ini
pengguna_lama = ['yaya', 'lala', 'admin', 'adel', 'amel']

# Daftar pengguna baru yang ingin mendaftar (beberapa ada yang sama dengan pengguna lama dengan variasi huruf)
pengguna_baru = ['Yaya', 'Lala', 'ael', 'yusrin', 'adel']

# Uabah dari pengguna_lama dalam bentuk huruf kecil
pengguna_lama_kecil = [nama.lower() for nama in pengguna_lama]

for pengguna_b in pengguna_baru:
    # Pemeriksa apakah nama pengguna baru sudah ada di daftar lama (dalam huruf kecil)
    if pengguna_b.lower() in pengguna_lama_kecil:
        print(f"Maaf, nama '{pengguna_b}' sudah digunakan. Anda harus memasukkan nama pengguna baru.")
    else:
        print(f"Nama pengguna '{pengguna_b}' tersedia.")