# 1
orang_1 = {
    'nama_depan': 'alnakhaila',
    'nama_belakang': 'fitri',
    'usia': 19,
    'kota': 'jakarta',
    'hobi': 'membaca',
    'warna_favorit': 'biru'
}


# 2
orang_2 = {
    'nama_depan': 'alnakhaira',
    'nama_belakang': 'putri',
    'usia': 19,
    'kota': 'bandung',
    'hobi': 'memasak',
    'warna_favorit': "hijau"
}

# 3
orang_3 = {
    'nama_depan': 'nissa',
    'nama_belakang': 'putri',
    'usia': 18,
    'kota': 'surabaya',
    'hobi': 'tertawa',
    'warna_favorit': 'biru'
}

people = [orang_1, orang_2, orang_3]


for person in people:
    nama_lengkap = f"{person['nama_depan']} {person['nama_belakang']}"
    print(f"\nNama Lengkap: {nama_lengkap.title()}")
    print(f"Usia: {person['usia']} tahun")
    print(f"Kota: {person['kota'].title()}")
    print(f"Warna Favorit: {person['warna_favorit'].title()}")
    print(f"Hobi: {person['hobi'].title()}")
