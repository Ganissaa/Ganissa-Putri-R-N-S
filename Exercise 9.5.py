class User:
    def __init__(self, first_name, last_name, age, username, location):
        "Inisialisasi profil pengguna termasuk atribut login_attempts."
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        self.location = location
        self.login_attempts = 0  # Atribut baru dengan nilai awal 0

    def describe_user(self):
        print(f" Ringkasan Profil Pengguna ")
        print(f"Nama Lengkap : {self.first_name} {self.last_name}")
        print(f"Nama Pengguna: {self.username}")
        print(f"Usia         : {self.age} tahun")
        print(f"Lokasi       : {self.location}")

    def greet_user(self):
        print(f"Halo, selamat datang kembali, {self.first_name} {self.last_name}!\n")

    def increment_login_attempts(self):
        "Method untuk menambah nilai login_attempts sebanyak 1."
        self.login_attempts += 1

    def reset_login_attempts(self):
        "Method untuk mereset nilai login_attempts kembali menjadi 0."
        self.login_attempts = 0


# Membuat instance dari kelas User
user_1 = User("Ael","Putri", 18, "Ael_Putri9", "Jakarta")

# Memanggil increment_login_attempts() beberapa kali
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

# Mencetak nilai login_attempts untuk memastikan bertambah dengan benar
print(f"Jumlah percobaan login setelah beberapa kali increment: {user_1.login_attempts}")

# Memanggil reset_login_attempts()
user_1.reset_login_attempts()

# Mencetak login_attempts lagi untuk memastikan sudah di-reset ke 0
print(f"Jumlah percobaan login setelah di-reset: {user_1.login_attempts}")