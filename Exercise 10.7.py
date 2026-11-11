print(" Kalkulator Penjumlahan (Ketik 'keluar' untuk berhenti) ")

while True:
    angka_pertama = input("\nMasukkan angka pertama: ")
    if angka_pertama.lower() == 'keluar':
        break
        
    angka_kedua = input("Masukkan angka kedua: ")
    if angka_kedua.lower() == 'keluar':
        break
        
    try:
        # Mengonversi input menjadi float untuk dijumlahkan
        hasil = float(angka_pertama) + float(angka_kedua)
    except ValueError:
        print("Error: Harap masukkan angka yang valid. Silakan coba lagi.")
    else:
        print(f"Hasil penjumlahan: {hasil}")