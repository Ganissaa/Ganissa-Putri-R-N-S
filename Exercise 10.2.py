from pathlib import Path
jalur = Path ('belajar_python.txt')

isi = jalur.read_text()
daftar_baris = isi.splitlines()

for baris in daftar_baris :
    daftar_baru  = baris.replace("Python", "C")
    print(daftar_baru)