sungai_besar = {
    'sungai nil': 'mesir',
    'sungai amazon': 'brasil',
    'sungai yangtze': 'china'
}

# Menggunakan loop untuk mencetak kalimat tentang masing-masing sungai
print("--- Informasi Sungai ---")
for sungai, negara in sungai_besar.items():
    print(f"{sungai.title()} mengalir melalui negara {negara.title()}.")

# Menggunakan loop untuk mencetak nama setiap sungai
print("\nDaftar Nama Sungai:")
for sungai in sungai_besar.keys():
    print(f"- {sungai.title()}")

# Menggunakan loop untuk mencetak nama setiap negara
print("\nDaftar Nama Negara:")
for negara in sungai_besar.values():
    print(f"- {negara.title()}")