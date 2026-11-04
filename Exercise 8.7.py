def make_album(nama_artis, judul_album, jumlah_lagu=None):
    album = {
        'artis': nama_artis,
        'album': judul_album
    }
    
    # Jika jumlah lagu diisi, tambahkan ke dalam kamus
    if jumlah_lagu:
        album['jumlah_lagu'] = jumlah_lagu
        
    return album

# Membuat 3 kamus berbeda menggunakan fungsi
album_pertama = make_album("tulus", "monokrom")
album_kedua = make_album("noah", "separuh aku")
album_ketiga = make_album("mahalini", "mahalini", 8) 

print(album_pertama)
print(album_kedua)
print(album_ketiga)