from pathlib import Path
jalur = Path("belajar_python.txt")
isi = jalur.read_text()
print(isi)

daftar_baris = isi.splitlines()
print("menampilkan menggunakan perulangan")
for baris in daftar_baris :
    print(baris)