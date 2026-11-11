# Mengimpor kelas Restaurant dari file Restaurant.py
from Restaurant import Restaurant

# Membuat instance dari kelas Restaurant
restoran_favorit = Restaurant("Bahari", "Masakan Padang")

# Memanggil method untuk membuktikan impor berhasil
print(" Imported Restaurant ")
restoran_favorit.describe_restaurant()
restoran_favorit.open_restaurant()