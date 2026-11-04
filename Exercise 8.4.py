# Fungsi dengan nilai default pada parameter
def make_shirt(ukuran='L', pesan='I love U'):
    print(f"Membuat kaos ukuran {ukuran.upper()} dengan tulisan: '{pesan}'.")

# Membuat kaos ukuran besar (large) dengan pesan default
make_shirt()

# Membuat kaos ukuran sedang (medium) dengan pesan default
make_shirt(ukuran='M')

# Membuat kaos ukuran kecil dengan pesan yang berbeda
make_shirt(ukuran='S', pesan='Hidup mahasiswa')