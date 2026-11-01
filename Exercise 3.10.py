gunung = ["Semeru", "Rinjani", "Merapi"]
print("Daftar awal gunung:", gunung)

# Menggunakan append() untuk menambah di akhir
gunung.append("Kerinci")
print("Setelah append('Kerinci'):", gunung)

# Menggunakan insert() untuk menambah di posisi tertentu
gunung.insert(1, "Kerinci")
print("Setelah insert(1, 'Kerinci'):", gunung)

# Menggunakan del untuk menghapus berdasarkan indeks
del gunung[0]
print("Setelah del indeks 0:", gunung)

# Menggunakan pop() untuk menghapus elemen terakhir (dan menyimpannya)
gunung_terakhir = gunung.pop()
print(f"Setelah pop(), menghapus '{gunung_terakhir}':", gunung)

# Menggunakan remove() untuk menghapus berdasarkan nama nilai
gunung.remove("Merapi")
print("Setelah remove('Merapi'):", gunung)

# Menambahkan kembali beberapa nama agar variasi fungsi terlihat
gunung.extend(["Agung", "Lawu"])
print("List ditambah kembali:", gunung)

# Menggunakan sorted() untuk melihat urutan sementara
print("Urutan sementara (sorted):", sorted(gunung))
print("List asli tetap tidak berubah:", gunung)

# Menggunakan sort() untuk mengurutkan secara permanen
gunung.sort()
print("Setelah sort() permanen (A-Z):", gunung)

# Menggunakan len() untuk menghitung jumlah item dalam list
print(f"Total gunung yang tersisa di list ada {len(gunung)} buah.")