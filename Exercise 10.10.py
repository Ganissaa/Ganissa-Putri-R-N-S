def hitung_kata_the(nama_file):
    "Menghitung kemunculan kata 'the' di dalam file teks."
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            teks = file.read()
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")
    else:
        # Mengubah teks menjadi huruf kecil agar kata 'The' atau 'THE' ikut terhitung
        # Menggunakan 'the ' (dengan spasi) untuk mencari kata secara lebih spesifik
        jumlah_kata = teks.lower().count('the ')
        print(f"Kata 'the' (dengan spasi) muncul sebanyak {jumlah_kata} kali di dalam {nama_file}.")
        
        # Jika ingin menghitung semua huruf 'the' termasuk di dalam kata lain (seperti 'then', 'there')
        jumlah_total = teks.lower().count('the')
        print(f"Substring 'the' secara umum muncul sebanyak {jumlah_total} kali.")

# Jalankan fungsi
hitung_kata_the('Dongeng.txt')