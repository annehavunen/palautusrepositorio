from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        tavaroita = 0
        for ostos in self._ostokset:
            tavaroita += ostos.lukumaara()
        return tavaroita

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        hinta = 0
        for ostos in self._ostokset:
            lukumaara = ostos.lukumaara()
            hinta += lukumaara * ostos.tuote.hinta()
        return hinta
        
    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        uusi_ostos = Ostos(lisattava)
        loytyy = False
        for ostos in self._ostokset:
            if ostos.tuote.nimi() == uusi_ostos.tuote.nimi() and ostos.tuote.hinta() == uusi_ostos.tuote.hinta():
                loytyy = True
                ostos.muuta_lukumaaraa(1)
        if not loytyy:
            self._ostokset.append(uusi_ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for ostos in self._ostokset:
            if ostos.tuote.nimi() == poistettava.nimi() and ostos.tuote.hinta() == poistettava.hinta():
                ostos.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        # tyhjentää ostoskorin
        pass

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self._ostokset
