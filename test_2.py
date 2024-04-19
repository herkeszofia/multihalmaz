class MultiHalmaz:
    def __init__(self):
        self.elemek = {}

    def hozzaad(self, elem, darab):
        if elem in self.elemek:
            self.elemek[elem] += darab
        else:
            self.elemek[elem] = darab

    def eltavolit(self, elem, darab):
        if elem in self.elemek:
            if self.elemek[elem] <= darab:
                del self.elemek[elem]
            else:
                self.elemek[elem] -= darab

    def unio(self, masik_halmaz):
        eredmeny = MultiHalmaz()
        for elem, darab in self.elemek.items():
            eredmeny.elemek[elem] = darab
        for elem, darab in masik_halmaz.elemek.items():
            if elem in eredmeny.elemek:
                eredmeny.elemek[elem] = max(eredmeny.elemek[elem], darab)
            else:
                eredmeny.elemek[elem] = darab
        return eredmeny

    def metszet(self, masik_halmaz):
        eredmeny = MultiHalmaz()
        for elem, darab in self.elemek.items():
            if elem in masik_halmaz.elemek:
                eredmeny.elemek[elem] = min(darab, masik_halmaz.elemek[elem])
        return eredmeny

    def maximum(self):
        if not self.elemek:
            return None
        return max(self.elemek)

    def minimum(self):
        if not self.elemek:
            return None
        return min(self.elemek)

    def darabszam(self, elem):
        return self.elemek.get(elem, 0)

    def __contains__(self, elem):
        return elem in self.elemek

    def ures_e(self):
        return len(self.elemek) == 0

    def diszjunkt_e(self, masik_halmaz):
        return not any(elem in masik_halmaz.elemek for elem in self.elemek)

    def kiir(self):
        print("MultiHalmaz elemei:")
        for elem, darab in self.elemek.items():
            print(f"{elem}: {darab}")

# Felhasználótól adatok bekérése
print("Adja meg az első halmaz elemeit: ")
halmaz1 = MultiHalmaz()
while True:
    elem = input("Adjon meg egy elemet (vagy üssön Enter-t a befejezéshez): ")
    if not elem:
        break
    darab = int(input("Adja meg az elem darabszámát: "))
    halmaz1.hozzaad(elem, darab)

print("Adja meg a második halmaz elemeit: ")
halmaz2 = MultiHalmaz()
while True:
    elem = input("Adjon meg egy másik elemet (vagy üssön Enter-t a befejezéshez): ")
    if not elem:
        break
    darab = int(input("Adja meg az elem darabszámát: "))
    halmaz2.hozzaad(elem, darab)

# Tesztelés
print("Halmaz 1 elemei:")
halmaz1.kiir()

print("Halmaz 2 elemei:")
halmaz2.kiir()

print("Unió:")
unio_halmaz = halmaz1.unio(halmaz2)
unio_halmaz.kiir()

print("Metszet:")
metszet_halmaz = halmaz1.metszet(halmaz2)
metszet_halmaz.kiir()

print("Maximum halmaz 1-ben:", halmaz1.maximum())
print("Minimum halmaz 1-ben:", halmaz1.minimum())

keresett_elem = input("Adja meg az elemet, aminek a darabszámát szeretné tudni: ")
print(f"{keresett_elem} darabszáma halmaz 1-ben:", halmaz1.darabszam(keresett_elem))

keresett_elem = input("Adja meg az elemet, aminek a jelenlétét vizsgálja: ")
print(f"Tartalmazza-e a(z) {keresett_elem}-et a halmaz 1?", keresett_elem in halmaz1)

print("Halmaz 1 üres?", halmaz1.ures_e())
print("Halmaz 1 és halmaz 2 diszjunkt?", halmaz1.diszjunkt_e(halmaz2))
