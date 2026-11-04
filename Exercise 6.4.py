Istilah = {
    'dictionary': 'Struktur yang menyimpan data dalam bentuk pasangan kunci dan nilai (key-value).',
    'list': 'Kumpulan item yang disimpan secara berurutan dalam satu variabel.',
    'loop': 'Perulangan untuk menjalankan blok kode secara berulang-ulang.',
    'string': 'Deretan karakter yang diapit oleh tanda kutip.',
    'variable': 'Tempat menyimpan data di dalam memori komputer.',
    'integer': 'Tipe data untuk angka bulat.',
    'float': 'Tipe data untuk angka desimal atau pecahan.',
    'boolean': 'Tipe data khusus bernilai True (benar) atau False (salah).',
    'comment': 'Catatan dalam kode yang diabaikan oleh Python, diawali dengan tanda pagar (#).',
    'key': 'Nama atau penanda unik untuk mengakses nilai dalam sebuah dictionary.'
}

print("--- Istilah Pemrograman---") 
for kata, arti in Istilah.items():
    print(f"\n{kata.title()}:\n{arti}")