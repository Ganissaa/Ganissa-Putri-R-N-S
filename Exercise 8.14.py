# Fungsi make_car
def make_car(produsen, model, **info_lainnya):
    mobil = {
        'produsen': produsen,
        'model': model
    }
    
    # Menambahkan data tambahan 
    for kunci, nilai in info_lainnya.items():
        mobil[kunci] = nilai
        
    return mobil

# Memanggil fungsi
mobil = make_car('subaru', 'outback', color='blue', tow_package=True)

# Mencetak kamus yang dikembalikan untuk memastikan semua informasi tersimpan benar
print("\nInformasi Mobil:")
print(mobil)