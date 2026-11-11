# Kelas induk User dari latihan sebelumnya
class User:
    def __init__(self, first_name, last_name, age, username, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        self.location = location

    def describe_user(self):
        print(f"Nama Pengguna: {self.username} ({self.first_name} {self.last_name})")

    def greet_user(self):
        print(f"Halo, {self.first_name}!\n")


# Kelas anak Admin yang mewarisi User
class Admin(User):
    def __init__(self, first_name, last_name, age, username, location):
        "Inisialisasi atribut User dan menambahkan atribut privileges."
        super().__init__(first_name, last_name, age, username, location)
        self.privileges = ["can add post", "can delete post", "can ban user", "can approve user"]

    def show_privileges(self):
        "Method untuk menampilkan daftar hak akses admin."
        print(f"Hak akses untuk Admin {self.username}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Membuat instance dari Admin dan memanggil method-nya
admin_baru = Admin("Lala", "Fitri", 28, "lala_admin", "Bandung")
admin_baru.describe_user()
admin_baru.show_privileges()