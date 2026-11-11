from pathlib import Path
import json

path = Path('angka_favorit.json')

if path.exists():

    isi_json =path.read_text(encoding='utf-8')
    angka_favorit = json.loads(isi_json)
    print(f"Saya tahu angka favoritmu! Angkanya adalah{angka_favorit}.")
else :
    angka_favorit = input("Berapa angka favoritmu?")

    isi_json = json.dumps(angka_favorit)
    path.write_text(isi_json, encoding='utf-8')

    print("Terimakasih! Angka favoritmu telah disiman.")