'''
A feladat első fele az, hogy létre tudjunk hozni egy halmazt, amiben tárolhatjuk az adatokat.

Az __init__(self) = Létrehoz egy üres szótárat a self.elemek szótárat, és ebben tároljuk az elemeket.
A szótár kulcsai lesznek az elemek, a hozzájuk tartozó értékek pedig az elemek száma.

A hozzaad(self,elem) hozzá ad egy elemet a halmazhoz viszont, ha ez az elem, már
megtalálható a halmazunkban, akkkor csak megnöveli az elemek számát 1-gyel.

Az eltavolit(self, elem) az  a metódus, amelyik eltávolít egy elemet a halmazból, viszont,
ha ez az elem már benne volt a halmazban csak csökkenti az elemek számát 1-gyel.
Ha az adott elemek száma 1, és megint töröljük ugyanezt, akkor az elem teljesen törlődik a halmazból.
'''
class MultiHalmaz:
    def __init__(self):
        self.elemek = {}

    def hozzaad(self, elem):
        if elem in self.elemek:
            self.elemek[elem] += 1
        else:
            self.elemek[elem] = 1

    def eltavolit(self, elem):
        if elem in self.elemek:
            if self.elemek[elem] == 1:
                del self.elemek[elem]
            else:
                self.elemek[elem] -= 1

    '''
    A második feladat az, hogy elkezdjük programként felírni a 
    matematikában is jól használt halmazműveleteket is.
     Ezen műveletek a(z); unió, max, min, metszet, eleme, multiplicitás, mind közös, üres halmaz-e.
    '''
    def unio(self, masik_halmaz):
        eredmeny = MultiHalmaz()
        for elem in self.elemek:
            eredmeny.elemek[elem] = self.elemek[elem]
        for elem in masik_halmaz.elemek:
            if elem in eredmeny.elemek:
                eredmeny.elemek[elem] = max(eredmeny.elemek[elem], masik_halmaz.elemek[elem])
            else:
                eredmeny.elemek[elem] = masik_halmaz.elemek[elem]
        return eredmeny

    def metszet(self, masik_halmaz):
        eredmeny = MultiHalmaz()
        for elem in self.elemek:
            if elem in masik_halmaz.elemek:
                eredmeny.elemek[elem] = min(self.elemek[elem], masik_halmaz.elemek[elem])
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


# Tesztelés
halmaz1 = MultiHalmaz()
halmaz1.hozzaad(1)
halmaz1.hozzaad(2)
halmaz1.hozzaad(2)
halmaz1.hozzaad(3)
halmaz1.kiir()  # Kiírja: MultiHalmaz elemei: 1: 1, 2: 2, 3: 1

halmaz2 = MultiHalmaz()
halmaz2.hozzaad(2)
halmaz2.hozzaad(3)
halmaz2.hozzaad(3)
halmaz2.hozzaad(4)
halmaz2.kiir()  # Kiírja: MultiHalmaz elemei: 2: 1, 3: 2, 4: 1

print("Unió:")
unio_halmaz = halmaz1.unio(halmaz2)
unio_halmaz.kiir()  # Kiírja: MultiHalmaz elemei: 1: 1, 2: 2, 3: 2, 4: 1

print("Metszet:")
metszet_halmaz = halmaz1.metszet(halmaz2)
metszet_halmaz.kiir()  # Kiírja: MultiHalmaz elemei: 2: 1, 3: 1

print("Maximum:", halmaz1.maximum())  # Kiírja: Maximum: 3
print("Minimum:", halmaz1.minimum())  # Kiírja: Minimum: 1

print("2 darabszáma halmaz1-ben:", halmaz1.darabszam(2))  # Kiírja: 2 darabszáma halmaz1-ben: 2

print("Tartalmazza-e a 3-at halmaz1?", 3 in halmaz1)  # Kiírja: Tartalmazza-e a 3-at halmaz1? True

print("Halmaz1 üres?", halmaz1.ures_e())  # Kiírja: Halmaz1 üres? False
print("Diszjunkt-e halmaz1 és halmaz2?", halmaz1.diszjunkt_e(halmaz2))  # Kiírja: Diszjunkt-e halmaz1 és halmaz2? False
