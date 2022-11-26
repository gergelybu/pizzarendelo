tipus = []
meret = []
feltet = []
ar = []


def adatbekeres():
    rendelesmeg = "igen"
    while rendelesmeg != "nem":
        pizzatipus = input("Milyen pizzát kér? sajtos, gombás vagy sonkás ")
        pizzameret = input("Mekkora pizzát kér? kicsi, normál vagy nagy ")
        pizzafeltet = input("Kér-e extra feltétet? igen vagy nem ")
        rendelesmeg = input("Akar új rendelést rögzíteni? ")
        tipus.append(pizzatipus)
        meret.append(pizzameret)
        feltet.append(pizzafeltet)



def arszamitas():
    tipusar()
    meretar()
    feltetar()


def tipusar():
    i = 0
    while i < len(tipus):
        if tipus[i] == "sajtos":
            ar.append(1000)
        elif tipus[i] == "gombás":
            ar.append(1100)
        elif tipus[i] == "sonkás":
            ar.append(1200)
        i = i + 1


def meretar():
    i = 0
    while i < len(meret):
        if meret[i] == "kicsi":
            ar[i] = ar[i] * 0.9
        elif meret[i] == "normál":
            ar[i] = ar[i] * 1
        elif meret[i] == "nagy":
            ar[i] = ar[i] * 1.1
        i = i + 1


def feltetar():
    i = 0
    while i < len(tipus):
        if feltet[i] == "igen":
            ar[i] = ar[i] + 50
        i = i + 1


def rendeles_kiiras():
    i = 0
    while i < len(tipus):
        print(f"Rendelés adatai: \n {tipus[i]} pizza \n {meret[i]} méretű, \n {feltet[i]}, \n végösszeg: {ar[i]:.0f}")
        i = i + 1