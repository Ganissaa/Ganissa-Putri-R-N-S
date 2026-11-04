tempat_favorit = {
    'ael': ['pantai', 'gunung', 'warjaw'],
    'yusrin': ['kafe', 'komunal'],
    'domi': ['taman kota', 'mall']
}

for nama, tempat_list in tempat_favorit.items():
    print(f"\nTempat favorit {nama.title()} adalah:")
    for tempat in tempat_list:
        print(f"- {tempat.title()}")