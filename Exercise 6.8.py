
pet_1 = {
    'jenis_hewan': 'kucing',
    'nama_pemilik': 'yusrin'
}

pet_2 = {
    'jenis_hewan': 'anjing',
    'nama_pemilik': 'domi'
}

pet_3 = {
    'jenis_hewan': 'burung',
    'nama_pemilik': 'ael'
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"\nHewan ini adalah seekor {pet['jenis_hewan']}.")
    print(f"Pemiliknya adalah {pet['nama_pemilik'].title()}.")