class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        "Inisialisasi atribut nama restoran, jenis masakan, dan jumlah yang dilayani."
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Atribut baru dengan nilai default 0

    def describe_restaurant(self):
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restoran {self.restaurant_name} saat ini sedang buka!\n")

    def set_number_served(self, number):
        "Method untuk menetapkan jumlah pelanggan yang telah dilayani."
        self.number_served = number

    def increment_number_served(self, additional_customers):
        "Method untuk menambah jumlah pelanggan yang dilayani."
        self.number_served += additional_customers


# Membuat instance dari kelas Restaurant
restaurant = Restaurant("Bahari", "Masakan Padang")

# Mencetak jumlah pelanggan awal (default 0)
print(f"Jumlah pelanggan awal yang dilayani: {restaurant.number_served}")

# Mengubah nilai atribut secara langsung dan mencetaknya kembali
restaurant.number_served = 18
print(f"Jumlah pelanggan setelah diubah langsung: {restaurant.number_served}")

# Menggunakan method set_number_served()
restaurant.set_number_served(60)
print(f"Jumlah pelanggan setelah menggunakan set_number_served(60): {restaurant.number_served}")

# Menggunakan method increment_number_served() (misal bertambah berapa orang hari ini)
restaurant.increment_number_served(45)
print(f"Jumlah pelanggan setelah ditambah 45 orang: {restaurant.number_served}")