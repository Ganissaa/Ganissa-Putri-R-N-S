# Kelas User
class User:
    def __init__(self, first_name, last_name, age, username, location):
        "Inisialisasi atribut profil pengguna."
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        self.location = location

    def describe_user(self):
        "Method untuk mencetak ringkasan informasi pengguna."
        print(f" Ringkasan Profil Pengguna ")
        print(f"Nama Lengkap : {self.first_name} {self.last_name}")
        print(f"Nama Pengguna: {self.username}")
        print(f"Usia         : {self.age} tahun")
        print(f"Lokasi       : {self.location}")

    def greet_user(self):
        "Method untuk mencetak salam personal kepada pengguna."
        print(f"Halo, selamat datang kembali, {self.first_name} {self.last_name}!\n")


# Membuat beberapa instance dengan data pengguna yang berbeda
user_1 = User("Ael", "Putri", 18, "Ael_Putri9", "Jakarta")
user_2 = User("Dom", "Tara", 18, "Domi_Tara8", "Bandung")
user_3 = User("Yus", "Rin", 17, "yusrinnn9", "Surabaya")

# Memanggil kedua method untuk setiap pengguna
user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()