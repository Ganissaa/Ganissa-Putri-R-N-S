print("Masukkan topping pizza.")
print("Ketik 'quit' jika Anda sudah selesai.\n")

# Perulangan akan terus berjalan sampai pengguna mengetik 'quit'
while True:
    topping = input("Masukkan topping: ")
    
    # Apakah pengguna ingin keluar
    if topping.lower() == 'quit':
        print("\nProgram selesai. Selamat menikmati pizza!")
        break
    else:
        print(f"-> Baik, saya akan menambahkan {topping} ke pizza Anda!\n")