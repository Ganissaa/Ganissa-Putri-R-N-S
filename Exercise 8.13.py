def build_profile(nama_depan, nama_belakang, **info_tambahan):
    profil = {}
    profil['nama_depan'] = nama_depan
    profil['nama_belakang'] = nama_belakang
    
    # Memasukkan semua data tambahan ke dalam kamus profil
    for kunci, nilai in info_tambahan.items():
        profil[kunci] = nilai
        
    return profil

# Memanggil fungsi untuk membuat profil diri sendiri
profil_dia = build_profile(
    'Yusrina', 
    'Putri', 
    pekerjaan='mahasiswa', 
    hobi='Nonton', 
    lokasi='jakarta'
)

# Mencetak hasil profil yang dikembalikan
print("Profil Pengguna:")
print(profil_dia)