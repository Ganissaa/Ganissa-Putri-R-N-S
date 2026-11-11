from random import randint

class Die:
    def __init__(self, sides=6):
        "Inisialisasi jumlah sisi dadu (default 6 sisi)."
        self.sides = sides

    def roll_die(self):
        "Method untuk melempar dadu dan mencetak angka acak antara 1 dan jumlah sisi."
        hasil = randint(1, self.sides)
        print(f"Hasil lemparan dadu {self.sides} sisi: {hasil}")


# Membuat dadu bersisi 6 dan melemparnya 10 kali
print(" Lemparan Dadu 6 Sisi (10 kali) ")
dadu_6 = Die()
for _ in range(10):
    dadu_6.roll_die()

# Membuat dadu bersisi 10 dan melemparnya 10 kali
print("\n Lemparan Dadu 10 Sisi (10 kali) ")
dadu_10 = Die(10)
for _ in range(10):
    dadu_10.roll_die()

# Membuat dadu bersisi 20 dan melemparnya 10 kali
print("\n Lemparan Dadu 20 Sisi (10 kali) ")
dadu_20 = Die(20)
for _ in range(10):
    dadu_20.roll_die()