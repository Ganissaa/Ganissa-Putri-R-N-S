from random import choice

# Daftar item lotre
item_lotre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# Tiket pilihan Anda (my_ticket)
my_ticket = [7, 'b', 3, 10]

jumlah_penarikan = 0
menang = False

print(" Analisis Lotre (Sedang Mencari Tiket Pemenang...) ")

while not menang:
    jumlah_penarikan += 1
    
    # Menarik 4 item acak untuk undian saat ini
    undian_sekarang = []
    while len(undian_sekarang) < 4:
        pilihan = choice(item_lotre)
        if pilihan not in undian_sekarang:
            undian_sekarang.append(pilihan)
            
    # Periksa apakah tiket kita cocok (menggunakan set agar urutan tidak masalah)
    if set(undian_sekarang) == set(my_ticket):
        menang = True

print(f"Selamat! Tiket Anda ({my_ticket}) cocok dengan hasil undian.")
print(f"Loop harus berjalan sebanyak **{jumlah_penarikan:,} kali** untuk memberikan Anda tiket yang menang.")