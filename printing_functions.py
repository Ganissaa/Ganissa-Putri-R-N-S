def cetak_model(daftar_desain, model_selesai):
    while daftar_desain:
        desain_sekarang = daftar_desain.pop()
        print(f"Sedang mencetak model: {desain_sekarang}")
        model_selesai.append(desain_sekarang)

def tampilkan_model_selesai(model_selesai):
    print("\nModel berikut telah selesai dicetak:")
    for model in model_selesai:
        print(f"- {model}")