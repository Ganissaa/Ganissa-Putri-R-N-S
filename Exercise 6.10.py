nomor_favorit = {
    'lala': [7, 19, 21],
    'yaya': [102, 5],
    'adel': [3, 9, 67, 8],
    'amel': [9,98],
    'yusrin': [95, 10]
}

for nama, angka_list in nomor_favorit.items():
    print(f"\nNomor favorit {nama.title()} adalah:")
    for angka in angka_list:
        print(f"- {angka}")