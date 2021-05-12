import Pseudochess as pc
import ast

plik = open('auto.txt', 'r+')
linie = plik.readlines()
i = 0
zapisy_stanu_planszy = []
zapisy_mozliwych_ruchow = []
for linia in linie:
    linia = linia.replace('\n', '')
    linie[i] = linia
    if linia.startswith('p'):

        zapisy_stanu_planszy.append(ast.literal_eval(linia.replace('p', '')))
    elif linia.startswith('r'):
        zapisy_mozliwych_ruchow.append(ast.literal_eval(linia.replace('r', '')))

print(zapisy_stanu_planszy)
print(zapisy_mozliwych_ruchow)


i += 1



def gra():
    pc.wypisz_plansze()
    while True:
        pc.znajdz_pionki()
        pc.znajdz_ruch_g()
        pc.ruch_g()
        pc.czy_koniec()
        pc.znajdz_pionki()
        pc.znajdz_ruch_k()
        if pc.plansza not in zapisy_stanu_planszy:
            plik.write('p' + str(pc.plansza) + '\n')
            plik.write('r' + str(pc.znajdz_ruch_k()) + '\n\n')
        pc.ruch_k()
        pc.czy_koniec()


gra()

plik.close()
