# Program lanjutan dari daftar tamu sebelumnya (6 orang)
daftar_tamu  = ["Ael ", "Lala", " Yusrin", "Yaya", "Nissa", "Lana"]

print("\n[Info] Meja besar tidak datang tepat waktu. Kami hanya dapat mengundang dua orang.\n")

# Mengeluarkan tamu satu per satu menggunakan pop() hingga tersisa 2 orang
while len(daftar_tamu) > 2:
    tamu_dibatalkan = daftar_tamu.pop()
    print(f"Maaf {tamu_dibatalkan}, kami tidak bisa mengundang Anda ke makan malam.")

print("\n=== TAMU YANG TETAP DIUNDANG ===")
print(f"Halo {daftar_tamu[0]}, Anda masih diundang.")
print(f"Halo {daftar_tamu[1]}, Anda masih diundang.")

# Menghapus dua nama terakhir menggunakan del agar list kosong
del daftar_tamu[0]
del daftar_tamu[0]

print(f"\nDaftar tamu akhir (harus kosong): {daftar_tamu}")