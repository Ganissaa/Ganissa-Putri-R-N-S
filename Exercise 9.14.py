from random import choice

# Membuat daftar berisi 10 angka dan 5 huruf
item_lotre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# Memilih 4 item secara acak tanpa duplikasi
pemenang = []
while len(pemenang) < 4:
    pilihan = choice(item_lotre)
    if pilihan not in pemenang:
        pemenang.append(pilihan)

print(" Undian Lotre ")
print(f"Kombinasi angka/huruf pemenang adalah: {pemenang}")
print("Pesan: Tiket apa pun yang cocok dengan 4 angka atau huruf ini memenangkan hadiah!")