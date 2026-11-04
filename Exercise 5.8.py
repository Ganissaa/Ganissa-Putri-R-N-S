# Membuat daftar nama pengguna termasuk 'admin'
daftar_pengguna = ['admin', 'yaya', 'lala', 'adel', 'amel']

for pengguna in daftar_pengguna:
    if pengguna == 'admin':
        print(f" Halo admin, apakah Anda ingin melihat laporan status?")
    else:
        print(f" Halo {pengguna}, terima kasih sudah masuk kembali.")