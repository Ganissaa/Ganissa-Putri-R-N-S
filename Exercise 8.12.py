# Bahan
def buat_sandwich(*bahan):
    print("\nMembuat sandwich dengan bahan-bahan berikut:")
    for item in bahan:
        print(f"- {item}")
    print("Sandwich kamu sudah siap!")

# Fungsi sebanyak 3 kali dengan jumlah bahan yang berbeda
buat_sandwich('keju', 'selada', 'tomat')
buat_sandwich('daging sapi', 'keju')
buat_sandwich('ayam crispy', 'telur', 'timun', 'saus sambal', 'mayones')