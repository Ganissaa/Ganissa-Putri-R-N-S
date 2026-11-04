def make_album(nama_artis, judul_album, jumlah_lagu=None):
    album = {'artis': nama_artis, 'album': judul_album}
    if jumlah_lagu:
        album['jumlah_lagu'] = jumlah_lagu
    return album

print("Program Pendataan Album Musik")
print("(Ketik 'quit' kapan saja untuk keluar)\n")

# Perulangan while untuk meminta input dari pengguna
while True:
    artis = input("Masukkan nama artis: ")
    if artis.lower() == 'quit':
        break
        
    judul = input("Masukkan judul album: ")
    if judul.lower() == 'quit':
        break
        
    # Memanggil fungsi make_album 
    album_user = make_album(artis, judul)
    
    print("\nKamus album yang berhasil dibuat:")
    print(album_user)
    print("-" * 35)

print("\nTerima kasih! Program selesai.")