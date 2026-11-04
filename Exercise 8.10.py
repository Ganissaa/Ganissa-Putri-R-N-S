daftar_pesan = [
    "Halo, gimana kabarmu?", 
    "Jangan lupa makan buah.", 
    "Semangat yaa!"
]

pesan_terkirim = []

def send_message(pesan_masuk, pesan_keluar):
    while pesan_masuk:
        pesan_saat_ini = pesan_masuk.pop(0)
        print(f"mengirim pesan: {pesan_saat_ini}")
        pesan_keluar.append(pesan_saat_ini)

# Panggil send_massage
send_message(daftar_pesan, pesan_terkirim)

print("\n Status Akhir ")
print("list awal (daftar_pesan):", daftar_pesan)
print("list baru (pesan_terkirim):", pesan_terkirim)

