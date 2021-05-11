import Pseudochess as pc

plik = open('auto.txt', 'r+')
linie = plik.readlines()
i=0
for linia in linie:
    linie[i] = linia.replace('\n', '')
    i+=1

print(linie)
def gra():
    pc.wypisz_plansze()
    while True:
        pc.znajdz_pionki()
        pc.znajdz_ruch_g()
        pc.ruch_g()
        pc.czy_koniec()
        pc.znajdz_pionki()
        pc.znajdz_ruch_k()
        plik.write(str(pc.plansza)+'\n')
        plik.write(str(pc.znajdz_ruch_k())+'\n\n')
        pc.ruch_k()
        pc.czy_koniec()


gra()

plik.close()
