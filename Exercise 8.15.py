import printing_functions as pf

# Daftar desain yang akan dicetak dan daftar penampung
desain_tersedia = ['casing ponsel', 'robot mainan', 'dudukan']
model_jadi = []


pf.cetak_model(desain_tersedia, model_jadi)
pf.tampilkan_model_selesai(model_jadi)