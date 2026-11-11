class User:
    def __init__(self, first_name, last_name, age, username, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        self.location = location

    def describe_user(self):
        print(f"Nama Pengguna: {self.username} ({self.first_name} {self.last_name})")


# Kelas terpisah untuk mengelola hak akses
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        "Method dipindahkan ke kelas Privileges."
        print("Daftar Hak Akses:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, username, location):
        super().__init__(first_name, last_name, age, username, location)
        # Menjadikan instance Privileges sebagai atribut di dalam kelas Admin
        self.privileges = Privileges()


# Membuat instance baru dari Admin dan menggunakan method-nya
admin_utama = Admin("Rara", "Putri", 26, "rara_admin", "Surabaya")
admin_utama.describe_user()
admin_utama.privileges.show_privileges()