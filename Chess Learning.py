import Pseudochess as pc
import ast

plik = open('auto.txt', 'r+')
zawartosc_pliku = plik.readlines()
i = 0
linie = []
zapisy_stanu_planszy = []
zapisy_mozliwych_ruchow = []
for linia in zawartosc_pliku:
    linia = linia.replace('\n', '')
    linie.append(linia)
    if linia.startswith('p'):

        zapisy_stanu_planszy.append(ast.literal_eval(linia.replace('p', '')))
    elif linia.startswith('r'):
        zapisy_mozliwych_ruchow.append(ast.literal_eval(linia.replace('r', '')))
    i += 1
print(zapisy_stanu_planszy)
print(zapisy_mozliwych_ruchow)
print(linie)
for x in zawartosc_pliku:
    print(x)
    if '(1, 0)' in x:
        print('karamba!')






def gra():
    pc.wygrana = ''
    pc.wypisz_plansze()
    while True:
        pc.znajdz_pionki()
        pc.znajdz_ruch_g()
        pc.ruch_g()
        if pc.wygrana == 'g':
            plik.write(str(zawartosc_pliku))
            gra()
        pc.czy_koniec()
        if pc.wygrana == 'g':
            plik.write(str(zawartosc_pliku))
            gra()
        pc.znajdz_pionki()
        pc.znajdz_ruch_k()
        if pc.plansza not in zapisy_stanu_planszy:
            plik.write('p' + str(pc.plansza) + '\n')
            plik.write('r' + str(pc.znajdz_ruch_k()) + '\n\n')
        pc.ruch_k()
        if pc.wygrana == 'g':
            plik.write(str(zawartosc_pliku))
            gra()
        pc.czy_koniec()
        if pc.wygrana == 'g':
            plik.write(str(zawartosc_pliku))
            gra()


gra()

plik.close()
