"""Klasa, w ktorej mozna zrealizowac rozwiazanie Zadania 2"""

import uklad
import wykresy
import iteracjaprosta
import iteracjaseidela
import pagerank
import potegowa
import numpy as np


class Zadanie2:

    def __init__(self):
        """Konstruktor"""
        self.k = 7            # liczba pomiarow dla jednej wartosci parametru
        self.norma = 0
        self.n = 150

    def testy(self):
        """Testy wstepne"""

        # ustalam norme
        norma0 = 0
        # okreslam liczbe iteracji
        eps = 1e-1
        # zadaje uklad o rozmiarze n
        P = pagerank.PageRank(self.n)
        # losuje macierz przejscia podajac parametr gamma
        P.losuj(0.4)
        # wyswietlam srednia liczbe linkow
        print(f"Srednia liczba linkow: {P.srednia_liczba_linkow()}")
        # rozwiazuje problem metoda iteracji Seidela
        P.przygotuj_do_iteracji()
        # tworze obiekt klasy IteracjaSeidela i przekazuje tam
        # zmodyfikowany uklad - v
        test3 = iteracjaseidela.IteracjaSeidela(P.v)
        test3.przygotuj()
        # wykonuje zadana liczbe iteracji
        iter3 = test3.iteruj_roznica(eps=eps, norma=norma0)
        # wypisuje rozwiazanie - wektor wlasny bez ostatniej wspolrzednej
        test3.wypisz_rozwiazanie(iter)
        # sprwadzam jego niedokladnosc
        niedokladnosc3 = test3.sprawdz_rozwiazanie(norma=norma0)
        # wyswietlam ranking stron
        print("\nMetoda Seidela")
        P.ranking_po_iteracji(test3.X)
        print("Liczba iteracji: ", iter3)
        print("Niedokladnosc: ", niedokladnosc3)
        # miejsce na rozwiazanie pierwszej czesci zadania 2

        print("\nMetoda Potegowa")
        test2 = potegowa.Potegowa(P.u)
        iter2 = test2.iteruj_roznica(eps=eps)
        test2.wypisz_rozwiazanie(iter2)
        # sprwadzam jego niedokladnosc
        niedokladnosc2 = test2.sprawdz_rozwiazanie(norma=norma0)
        # wyswietlam ranking stron
        P.ranking(test2.y)
        print("Liczba iteracji: ", iter2)
        print("Niedokladnosc: ", niedokladnosc2)

        return 0

    def badaj_zbieznosc(self, epsilon=1e-13):
        """Badam zbieznosc metody iteracji seidela"""
        # ustalam zbior parametrow
        param = [1e-13, 1e-12, 1e-11, 1e-10, 1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
        # okreslam uklad rownan
        u1 = uklad.Uklad(wymiar=self.n)
        # dla kazdej wartosci parametru przeprowadzam po k testow
        # i wyswietlam wartosci wybranych charakterystyk eksperymentu
        sr_liczba_iteracji3 = []
        sr_liczba_iteracji2 = []
        sr_niedokladnosc3 = []
        sr_niedokladnosc2 = []
        for sk in param:
            liczba_iteracji = 0.0
            niedokladnosc3 = 0.0
            niedokladnosc2 = 0.0
            iteracje3 = 0
            iteracje2 = 0
            iteracje = 0
            while iteracje < self.k:
                # losujemy uklad

                # ustalam norme
                norma0 = 0
                # okreslam liczbe iteracji
                # zadaje uklad o rozmiarze n
                P = pagerank.PageRank(self.n)
                # losuje macierz przejscia podajac parametr gamma
                P.losuj(0.4)
                # wyswietlam srednia liczbe linkow
                print(f"Srednia liczba linkow: {P.srednia_liczba_linkow()}")
                # rozwiazuje problem metoda iteracji Seidela
                P.przygotuj_do_iteracji()
                # tworze obiekt klasy IteracjaSeidela i przekazuje tam
                # zmodyfikowany uklad - v
                test3 = iteracjaseidela.IteracjaSeidela(P.v)
                test3.przygotuj()
                # wykonuje zadana liczbe iteracji
                iter3 = test3.iteruj_roznica(eps=sk, norma=norma0)
                # wypisuje rozwiazanie - wektor wlasny bez ostatniej wspolrzednej
                # test3.wypisz_rozwiazanie(iter)
                # sprwadzam jego niedokladnosc
                niedokl3 = test3.sprawdz_rozwiazanie(norma=norma0)
                # wyswietlam ranking stron
                # print("\nMetoda Seidela")
                P.ranking_po_iteracji(test3.X)
                # print("Liczba iteracji: ", iter3)
                # print("Niedokladnosc: ", niedokladnosc3)
                # miejsce na rozwiazanie pierwszej czesci zadania 2

                # print("\nMetoda Potegowa")
                test2 = potegowa.Potegowa(P.u)
                iter2 = test2.iteruj_roznica(eps=sk)
                # test2.wypisz_rozwiazanie(iter2)
                # sprwadzam jego niedokladnosc
                niedokl2 = test2.sprawdz_rozwiazanie(norma=norma0)
                # wyswietlam ranking stron
                P.ranking(test2.y)
                # print("Liczba iteracji: ", iter2)
                # print("Niedokladnosc: ", niedokladnosc2)
                
                niedokladnosc3 += niedokl3
                niedokladnosc2 += niedokl2

                iteracje2 += iter2
                iteracje3 += iter3
                # liczba_iteracji += iter
                iteracje += 1
            # obliczam srednie wartosci charakterystyk
            sr_liczba_iteracji3.append(iteracje3/self.k)
            sr_liczba_iteracji2.append(iteracje2/self.k)
            sr_niedokladnosc3.append(niedokladnosc3/self.k)
            sr_niedokladnosc2.append(niedokladnosc2/self.k)
        # wypisujemy srednie charakterystyki
        print("Epsilon  Iteracje  Niedkoladnosc")
        print("------"*9)
        for i in range(len(param)):
            wyniki3 = f"{param[i]} \t"
            wyniki3 += f"{sr_liczba_iteracji3[i]} \t"
            wyniki3 += f"{sr_niedokladnosc3[i]:.6e} \n"
            print(wyniki3)

        print("Epsilon  Iteracje  Niedkoladnosc")
        print("------"*9)
        for i in range(len(param)):
            wyniki2 = f"{param[i]} \t"
            wyniki2 += f"{sr_liczba_iteracji2[i]} \t"
            wyniki2 += f"{sr_niedokladnosc2[i]:.6e} \n"
            print(wyniki2)

        return 0
