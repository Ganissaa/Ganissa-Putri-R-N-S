daftar_pizza = ['pepperoni', 'meat lovers', 'super supreme']

# Membuat salinan dari list daftar_pizza dan menamakannya menu_pizza           
menu_pizza = daftar_pizza[:]

# Menambahkan pizza baru daftar_pizza
daftar_pizza.append('chessy')
# Teman (menu_pizza)
menu_pizza.append('meat feast')

# pemisahan
print("Pizza favorit saya adalah:")
for pizza in daftar_pizza:
    print(f"- {pizza}")

print("\nPizza favorit teman saya adalah:")
for pizza in menu_pizza:
    print(f"- {pizza}")