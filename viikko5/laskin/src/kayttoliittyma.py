from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root

        self._komennot = {
            Komento.SUMMA: Summa(sovellus, self._lue_syote),
            Komento.EROTUS: Erotus(sovellus, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovellus),
            Komento.KUMOA: Kumoa(sovellus, self._hae_edellinen)
        }

    def kaynnista(self):
        self._edellinen = self._sovellus.tulos
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(
            columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        arvo = 0
        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass
        return arvo

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        if komento != Komento.KUMOA:
            self._edellinen = self._sovellus.tulos
        komento_olio.suorita()

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)

    def _hae_edellinen(self):
        return self._edellinen


class Komentotehdas:
    def __init__(self, sovellus, kutsuttava_funktio):
        self.sovellus = sovellus
        self.kutsuttava_funktio = kutsuttava_funktio

    def suorita(self):
        arvo = self.kutsuttava_funktio()
        self.tee_komento(arvo)

class Summa(Komentotehdas):
    def tee_komento(self, arvo):
        self.sovellus.plus(arvo)

class Erotus(Komentotehdas):
    def tee_komento(self, arvo):
        self.sovellus.miinus(arvo)


class Nollaus:
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self):
        self.sovellus.nollaa()


class Kumoa:
    def __init__(self, sovellus, hae_edellinen):
        self.sovellus = sovellus
        self.hae_edellinen = hae_edellinen

    def suorita(self):
        edellinen = self.hae_edellinen()
        self.sovellus.aseta_arvo(edellinen)
