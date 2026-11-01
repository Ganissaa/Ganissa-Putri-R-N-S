menu_makanan = ('ayam goreng', 'sup sayur', 'nasi putih', 'ikan bakar', 'mie goreng')
# yang ingin ditawarkan
print("Menu makanan awal di restoran:")
for makanan in menu_makanan:
    print(f"- {makanan}")

# Restoran mengubah menu dengan mengganti dua item dengan makanan yang berbeda
# Menulis ulang (menimpa) variabel tuple dengan nilai yang baru
menu_makanan = ('bebek goreng', 'sup sayur', 'nasi merah', 'ikan bakar', 'sate ayam')

# Menggunakan for loop untuk mencetak menu yang telah direvisi
print("\nMenu makanan setelah direvisi:")
for makanan in menu_makanan:
    print(f"- {makanan}")