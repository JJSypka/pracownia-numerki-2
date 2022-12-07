"""Klasa, w ktorej mozna zrealizowac rozwiazanie Zadania 1"""

import uklad, wykresy
import  iteracjaseidela
import numpy as np

class Zadanie1:

    def __init__(self):
        """Konstruktor"""
        self.n = 100          # wymiar macierzy
        self.norma = 1        # bede wykorzystywal norme kolumnowa
        self.k = 7             # liczba pomiarow dla jednej wartosci parametru        
        self.l = 50    #liczba iteracji w metodzie iteruj

    def testy(self):
        """Testy wstepne"""
        # miejsce na rozwiazanie pierwszej czesci zadania 1
        # """Zbieznosc/rozbieznosc metod iteracyjnych dla roznych macierzy"""
        u1 = uklad.Uklad(wymiar=self.n)
        u2 = uklad.Uklad(wymiar=self.n)

        # losujemy uklad
        u1.losuj_uklad_symetryczny_dodatnio_okreslony(alfa=0.2)
        u2.losuj_uklad_symetryczny_dodatnio_okreslony(alfa=2.6)

        # rozwiazuje uklad z wykorzystaniem metody iteracji Seidela
        test1 = iteracjaseidela.IteracjaSeidela(ukl=u1)
        test2 = iteracjaseidela.IteracjaSeidela(ukl=u2)
        # wyznaczam macierz D i wektor C
        test1.przygotuj()
        test2.przygotuj()
        #obliczam norme macierzy D
        norma_D1 = u1.norma_macierzy(typ=self.norma,macierz=test1.D)
        norma_D2 = u2.norma_macierzy(typ = self.norma, macierz=test2.D)
        # iteracja Seidela
        test1.iteruj(
            iteracje=self.l,
            norma=self.norma)
        test2.iteruj(
            iteracje=self.l,
            norma=self.norma)


        seria1 = test1.normy.copy()
        seria2 = test2.normy.copy()
        niedokl1 = test1.sprawdz_rozwiazanie(self.norma)
        print(f"Niedokladnosc rozwiazania1 - iteracja Seidela: {niedokl1}")
        print(f"Norma macierzy D1 - iteracja Seidela: {norma_D1}")
        
        niedokl2 = test2.sprawdz_rozwiazanie(self.norma)
        print(f"Niedokladnosc rozwiazania2 - iteracja Seidela: {niedokl2}")
        print(f"Norma macierzy D2 - iteracja Seidela: {norma_D2}")
        # rysuje obie serie na wykresie
        wykres_test = wykresy.Wykresy()
        wykres_test.badaj_zbieznosc(
            tytul="Zbieznosc metod iteracyjnych",
            opis_OY="Normy przyblizen",
            dane1=seria1,
            opis1="Iteracja Seidela mniejsze alfa",
            dane2=seria2,
            opis2="Iteracja Seidela wieksze alfa"
        )
        return 0
        
    def badaj_zbieznosc(self):
        """Badam zbieznosc metody iteracji seidela"""
        # ustalam zbior parametrow
        # param = [0.09, 0.18, 0.27, 0.36, 0.45, 0.54, 0.63, 0.72, 0.81, 0.9]
        param = [0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6]
        # okreslam uklad rownan
        u1 = uklad.Uklad(wymiar=self.n)
        # dla kazdej wartosci parametru przeprowadzam po k testow
        # i wyswietlam wartosci wybranych charakterystyk eksperymentu
        sr_liczba_iteracji = []
        sr_norma_macierzy = []
        sr_niedokladnosc = []
        for sk in param:
            norma_macierzy = 0.0
            liczba_iteracji = 0.0
            niedokladnosc = 0.0
            iteracje = 0
            while iteracje < self.k:
                # losujemy uklad
                u1.losuj_uklad_symetryczny_dodatnio_okreslony(alfa=sk)
                # rozwiazuje uklad z wykorzystaniem metody iteracji Seidela
                test1 = iteracjaseidela.IteracjaSeidela(ukl=u1)
                # wyznaczam macierz D i wektor C
                test1.przygotuj()
                # obliczam norma macierzy D
                norma_D = u1.norma_macierzy(
                    typ=self.norma,
                    macierz=test1.D)
                    #wykonuje zadana liczbe iteracji
                test1.iteruj(
                    iteracje=self.k,
                    norma=self.norma)
                niedokl = test1.sprawdz_rozwiazanie(norma=self.norma)
                norma_macierzy += norma_D
                niedokladnosc += niedokl
                # liczba_iteracji += iter
                iteracje += 1
            # obliczam srednie wartosci charakterystyk
            sr_norma_macierzy.append(norma_macierzy/self.k)
            sr_liczba_iteracji.append(liczba_iteracji/self.k)
            sr_niedokladnosc.append(niedokladnosc/self.k)
        # wypisujemy srednie charakterystyki
        print("Alfa \t ||D|| \t     Iteracje   Niedkoladnosc")
        print("------"*9)
        for i in range(len(param)):
            wyniki = f"{param[i]} \t"
            wyniki += f"{sr_norma_macierzy[i]:.6f} \t"
            wyniki += f"{self.k} \t"
            wyniki += f"{sr_niedokladnosc[i]:.6e} \n"
            print(wyniki)

        return 0

        