from pathlib import Path
import json

path = Path('user_profile.json')

if path.exists():
    isi_json = path.read_text(encoding='utf-8')
    profil_user = json.loads(isi_json)

    print("\n Selamat datang kembali ")
    print(f"berikut data yang tersimpan tentangmu:")
    print(f"- Nama      : {profil_user['nama']}")
    print(f"- Umur      : {profil_user['umur']}")
    print(f"- Kota Asal : {profil_user['kota']}")
    print(f"- Hobi      : {profil_user['hobi']}")

else:
    profil_user = {}

    profil_user['nama'] = input("Siapa nama kamu?")
    profil_user['umur'] = input("Berapa umur kamu?")
    profil_user['kota'] = input("Darimana asal kamu?")
    profil_user['Hobi'] = input("Apa hobi kamu?")

    isi_json = json.dumps(profil_user)
    path.write_text(isi_json, encoding='utf-8')

    print("\nTerimakasih! Informasi profilmu telah disimpan")