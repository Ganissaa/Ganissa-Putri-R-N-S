# Kelas Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        "Inisialisasi atribut nama restoran dan jenis masakan."
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        "Method untuk mencetak informasi restoran."
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Masakan: {self.cuisine_type}")

    def open_restaurant(self):
        "Method untuk mencetak status restoran."
        print(f"Restoran {self.restaurant_name} saat ini sedang buka!\n")


# Membuat objek bernama restaurant
restaurant = Restaurant("Bahari", "Masakan Padang")

# Mencetak atribut secara individual
print(" Mengakses Atribut Secara Individual ")
print("Nama restoran:", restaurant.restaurant_name)
print("Jenis masakan:", restaurant.cuisine_type)
print()

# Memanggil kedua method
print(" Memanggil Method ")
restaurant.describe_restaurant()
restaurant.open_restaurant()