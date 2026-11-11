# Kelas induk (Parent Class) dari latihan sebelumnya
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restoran {self.restaurant_name} saat ini sedang buka!\n")


# Kelas anak (Child Class) IceCreamStand yang mewarisi Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        "Inisialisasi atribut dari kelas induk, ditambah atribut flavors."
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Vanila', 'Cokelat', 'Stroberi', 'Matcha']

    def display_flavors(self):
        "Method untuk menampilkan daftar rasa es krim."
        print(f"Daftar rasa es krim di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Membuat instance dari IceCreamStand dan memanggil method-nya
kedai_es_krim = IceCreamStand("Es Krim MIMI")
kedai_es_krim.describe_restaurant()
kedai_es_krim.display_flavors()