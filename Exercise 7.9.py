# Daftar pesanan dengan 'pastrami' muncul beberapa kali
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'ayam', 'keju', 'pastrami']

print("Maaf, toko deli kami sedang kehabisan pastrami untuk hari ini!\n")

# Menghapus semua kemunculan 'pastrami' dari sandwich_orders menggunakan while loop
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Sandwich yang selesai
finished_sandwichies = []

# Memproses sisa pesanan
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Saya sedang membuat sandwich {current_sandwich} Anda.")
    finished_sandwichies.append(current_sandwich)

print("\nSisa sandwich berhasil dibuat tanpa pastrami!")
for finished in finished_sandwichies:
    print(f"- Sandwich {finished} sudah jadi.")