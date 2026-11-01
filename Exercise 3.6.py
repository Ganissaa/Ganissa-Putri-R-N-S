# Program lanjutan dari daftar tamu sebelumnya
daftar_tamu = ["Lala", "Yaya", "Nissa"]

print("\n[Info] Kabar gembira! Kami menemukan meja makan yang lebih besar.\n")

# Menambahkan tamu baru menggunakan insert() dan append()
daftar_tamu.insert(0, "Ael")          # Menambah di awal daftar
daftar_tamu.insert(2, "Yusrin")          # Menambah di tengah daftar
daftar_tamu.append("Lana")              # Menambah di akhir daftar

print("=== UNDANGAN UNTUK TAMU TAMBAHAN ===")
for tamu in daftar_tamu:
    print(f"Halo {tamu}, Anda diundang ke acara makan malam Adel.")