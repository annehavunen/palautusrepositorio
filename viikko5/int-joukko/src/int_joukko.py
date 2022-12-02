KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def paikka(self, luku):
        for i in range(0, self.alkioiden_lkm):
            if luku == self.lukujono[i]:
                return i
        return -1

    def kuuluu(self, luku):
        indeksi = self.paikka(luku)
        if indeksi == -1:
            return False
        return True

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False

        self.lukujono[self.alkioiden_lkm] = luku
        self.alkioiden_lkm += 1

        if self.alkioiden_lkm == len(self.lukujono):
            aputaulukko = self.lukujono
            self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_taulukko(aputaulukko, self.lukujono)

        return True

    def poista(self, luku):
        sijainti = self.paikka(luku)
        if sijainti == -1:
            return False
        self.siirra_yhdella_taaksepain(sijainti)
        return True

    def kopioi_taulukko(self, mista, mihin):
        for i in range(0, len(mista)):
            mihin[i] = mista[i]

    def siirra_yhdella_taaksepain(self, sijainti):
        for i in range(sijainti, self.alkioiden_lkm - 1):
            self.lukujono[i] = self.lukujono[i + 1]
        self.alkioiden_lkm -= 1

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()

        for alkio in a.to_int_list():
            yhdiste.lisaa(alkio)
        for alkio in b.to_int_list():
            yhdiste.lisaa(alkio)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()

        for alkio_a in a.to_int_list():
            for alkio_b in b.to_int_list():
                if alkio_a == alkio_b:
                    leikkaus.lisaa(alkio_b)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()

        for alkio in a.to_int_list():
            erotus.lisaa(alkio)
        for alkio in b.to_int_list():
            erotus.poista(alkio)

        return erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        mjono = "{"
        for i in range(0, self.alkioiden_lkm - 1):
            mjono += f"{str(self.lukujono[i])}, "
        mjono += str(self.lukujono[self.alkioiden_lkm - 1])
        mjono += "}"
        return mjono
