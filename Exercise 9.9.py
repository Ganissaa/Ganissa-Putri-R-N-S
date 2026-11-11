# Kelas dasar Car
class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.manufacturer.title()} {self.model.title()}"


# Kelas khusus untuk Battery
class Battery:
    def __init__(self, battery_size=30):
        "Inisialisasi ukuran baterai (default 30 kWh)."
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Mobil ini memiliki baterai berkapasitas {self.battery_size}-kWh.")

    def get_range(self):
        "Menghitung perkiraan jarak tempuh berdasarkan ukuran baterai."
        if self.battery_size == 30:
            range_km = 150
        elif self.battery_size == 75:
            range_km = 225
        else:
            range_km = 250

        print(f"Mobil ini dapat menempuh jarak sekitar {range_km} mil dengan sekali pengisian daya.")

    def upgrade_battery(self):
        "Method untuk meningkatkan kapasitas baterai menjadi 65 jika belum."
        if self.battery_size != 75:
            self.battery_size = 75
            print("Baterai berhasil ditingkatkan menjadi 75-kWh.")
        else:
            print("Baterai sudah berkapasitas maksimal.")


# Kelas ElectricCar yang mewarisi Car
class ElectricCar(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()  


on_tesla = ElectricCar('tesla', 'model s', 2023)

print(on_tesla.get_descriptive_name())
on_tesla.battery.describe_battery()

# Memanggil get_range() sebelum upgrade
on_tesla.battery.get_range()

# Melakukan upgrade baterai
on_tesla.battery.upgrade_battery()

# Memanggil get_range() sekali lagi untuk melihat peningkatan jarak
on_tesla.battery.get_range()