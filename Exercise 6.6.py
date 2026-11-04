# Dictionary orang-orang yang sudah mengisi polling sebelumnya
bahasa_favorit = {
    'ael': 'python',
    'yusrin': 'c',
    'lana': 'rust',
    'domi': 'python',
}

# Daftar orang yang harus mengikuti polling (ada yang sudah ada dan ada yang belum)
orang_yang_dipolling = ['ael', 'yusrin', 'lana', 'domi', 'vrysa', 'desy']

for nama in orang_yang_dipolling:
    if nama in bahasa_favorit:
        print(f"Terima kasih {nama.title()} karena sudah mengisi polling!")
    else:
        print(f"Halo {nama.title()}, Anda diundang untuk mengikuti polling bahasa pemrograman favorit.")