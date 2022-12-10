from tekoaly_parannettu import TekoalyParannettu
from kivi_paperi_sakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self._tekoaly = TekoalyParannettu(10)
        self._eka_kierros = True

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        if self._eka_kierros:
            self._eka_kierros = False
            return tokan_siirto

        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto
