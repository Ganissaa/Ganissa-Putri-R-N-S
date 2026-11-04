# Fungsi make_shirt dengan parameter ukuran dan pesan
def make_shirt(ukuran, pesan):
    """Fungsi untuk merangkum ukuran kaos dan pesan yang akan dicetak."""
    print(f"Membuat kaos ukuran {ukuran} dengan tulisan: '{pesan}'.")

# Panggil fungsi menggunakan positional arguments (berurutan)
make_shirt('M', 'Belajar itu Seru!')

# Panggil fungsi menggunakan keyword arguments (menyebutkan nama parameter)
make_shirt(ukuran='L', pesan='Kode Masa Depan')