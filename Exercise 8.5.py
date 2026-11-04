# Mendefinisikan fungsi dengan nilai default untuk parameter negara
def describe_city(kota, negara='China'):
    print(f"{kota} berada di negara {negara}.")

# Memanggil fungsi menggunakan negara default (Islandia)
describe_city('Thiangjai')

# Memanggil kota lain yang juga di Islandia
describe_city('Chianghai')

# Memanggil kota yang tidak berada di negara default (mengubah argumen negara)
describe_city('Jakarta', negara='Indonesia')