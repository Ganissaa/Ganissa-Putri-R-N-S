def city_country(nama_kota, nama_negara):
    return f"{nama_kota.title()}, {nama_negara.title()}"

# Memanggil fungsi dengan 3 pasangan kota dan negara berbeda
kota_1 = city_country("Jakarta", "Indonesia")
kota_2 = city_country("Tokyo", "Jepang")
kota_3 = city_country("Paris", "Prancis")

print(kota_1)
print(kota_2)
print(kota_3)