tempat_wisata = ["Jepang", "Swiss", "Kanada", "Amerika", "China"]

print("=== Urutan Asli ===")
print(tempat_wisata)

# Gunakan sorted() untuk mencetak urutan alfabet tanpa mengubah list asli
print("\n=== Urutan Alfabetis (Menggunakan sorted) ===")
print(sorted(tempat_wisata))

# Tunjukkan bahwa list masih dalam urutan aslinya
print("\n=== Kembali ke Urutan Asli ===")
print(tempat_wisata)

# Gunakan sorted() dengan reverse=True untuk urutan abjad terbalik (Z-A)
print("\n=== Urutan Abjad Terbalik (sorted dengan reverse=True) ===")
print(sorted(tempat_wisata, reverse=True))

# Tunjukkan bahwa list masih dalam urutan aslinya
print("\n=== Masih Urutan Asli ===")
print(tempat_wisata)

# Gunakan reverse() untuk membalikkan urutan list yang asli
tempat_wisata.reverse()
print("\n=== Setelah Dibalik (menggunakan reverse()) ===")
print(tempat_wisata)

# Gunakan reverse() lagi untuk mengembalikannya ke urutan semula
tempat_wisata.reverse()
print("\n=== Dikembalikan ke Urutan Asli ===")
print(tempat_wisata)

# Gunakan sort() untuk mengubah urutan list menjadi alfabet secara permanen
tempat_wisata.sort()
print("\n=== Diurutkan Secara Permanen (menggunakan sort()) ===")
print(tempat_wisata)

# Gunakan sort(reverse=True) untuk mengubah urutan menjadi Z-A secara permanen
tempat_wisata.sort(reverse=True)
print("\n=== Diurutkan Z-A Secara Permanen (sort dengan reverse=True) ===")
print(tempat_wisata)