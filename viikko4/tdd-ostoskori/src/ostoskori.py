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
        return len(self._ostokset)

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        if self._ostokset:
            return self._ostokset[0].tuote.hinta
        return 0
        
    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        uusi_ostos = Ostos(lisattava)
        self._ostokset.append(uusi_ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        # tyhjentää ostoskorin
        pass

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        pass
