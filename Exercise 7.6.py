print("Versi 1: Tes Kondisi di While")
topping = ""
while topping.lower() != 'quit':
    topping = input("Masukkan topping pizza (ketik 'quit' untuk berhenti): ")
    if topping.lower() != 'quit':
        print(f"Menambahkan {topping}...\n")
print("Program selesai.")

print("\nVersi 2: Menggunakan Variabel Aktif")
aktif = True
while aktif:
    topping = input("Masukkan topping pizza (ketik 'quit' untuk berhenti): ")
    if topping.lower() == 'quit':
        aktif = False
    else:
        print(f"Menambahkan {topping}...\n")
print("Program selesai.")

print("\nVersi 3: Menggunakan Break")
while True:
    topping = input("Masukkan topping pizza (ketik 'quit' untuk berhenti): ")
    if topping.lower() == 'quit':
        break
    print(f"Menambahkan {topping}...\n")
print("Program selesai.")