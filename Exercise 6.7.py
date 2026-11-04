# 1
orang_1 = {
    'nama_depan': 'alnakhaila',
    'nama_belakang': 'fitri',
    'usia': 19,
    'kota': 'jakarta'
}

# 2
orang_2 = {
    'nama_depan': 'alnakhaira',
    'nama_belakang': 'putri',
    'usia': 19,
    'kota': 'bandung'
}

# 3
orang_3 = {
    'nama_depan': 'nissa',
    'nama_belakang': 'putri',
    'usia': 18,
    'kota': 'surabaya'
}

people = [orang_1, orang_2, orang_3]


for person in people:
    nama_lengkap = f"{person['nama_depan']} {person['nama_belakang']}"
    print(f"\nNama Lengkap: {nama_lengkap.title()}")
    print(f"Usia: {person['usia']} tahun")
    print(f"Kota: {person['kota'].title()}")