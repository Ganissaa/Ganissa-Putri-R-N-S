from pathlib import Path
jalur = Path('belajar_python.txt')
isi = jalur.read_text()
print(isi)

print("setelah memakai perulangan")
for baris in isi.splitlines():
    print(baris)