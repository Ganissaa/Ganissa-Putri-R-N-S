# Daftar pesanan sandwich
sandwich_orders = ['tuna', 'ayam', 'keju', 'daging']

# Membuat daftar kosong untuk menampung sandwich yang sudah selesai dibuat
finished_sandwichies = []

# Proses
while sandwich_orders:
    # Pesanan pertama dari daftar sandwich_orders
    current_sandwich = sandwich_orders.pop(0)
    
    print(f"Saya sedang membuat sandwich {current_sandwich} Anda.")
    
    # Memindahkan sandwich yang sudah dibuat ke daftar finished_sandwichies
    finished_sandwichies.append(current_sandwich)

print("\nSemua sandwich telah selesai dibuat!")
# Menampilkan daftar sandwich yang sudah jadi
for finished in finished_sandwichies:
    print(f"- Sandwich {finished} sudah jadi.")