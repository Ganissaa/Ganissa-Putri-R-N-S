print("Selamat datang di Bioskop VIP!")
print("Ketik 'keluar' atau 'quit' untuk menghentikan program.\n")

while True:
    usia_input = input("Masukkan usia Anda: ")
    
    # Keluar jika pengguna mengetik 'quit' atau 'keluar'
    if usia_input.lower() in ['quit', 'keluar']:
        print("Terima kasih telah menggunakan layanan ini.")
        break
        
    # Mengubah teks menjadi angka
    usia = int(usia_input)
    
    # Menentukan harga tiket berdasarkan usia
    if usia < 3:
        print("-> Tiket Anda gratis!\n")
    elif 3 <= usia <= 12:
        print("-> Harga tiket Anda adalah $10.\n")
    else:
        print("-> Harga tiket Anda adalah $15.\n")