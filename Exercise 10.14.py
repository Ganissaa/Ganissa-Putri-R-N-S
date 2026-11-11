import json

nama_file = 'username.json'

def get_stored_username():
    "Mengambil nama pengguna yang tersimpan jika ada."
    try:
        with open(nama_file, 'r') as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    "Meminta nama pengguna baru."
    username = input("Siapa nama Anda? ")
    with open(nama_file, 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    "Menyambut pengguna dan memverifikasi apakah identitasnya sudah benar."
    username = get_stored_username()
    
    if username:
        # Memverifikasi apakah pengguna saat ini adalah orang yang benar
        cek = input(f"Apakah nama Anda {username}? (y/t): ")
        if cek.lower() == 'y':
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username()
            print(f"Baiklah, kami akan mengingat Anda sebagai {username}!")
    else:
        username = get_new_username()
        print(f"Kami akan mengingat Anda saat Anda kembali, {username}!")

# Menjalankan program verifikasi
greet_user()