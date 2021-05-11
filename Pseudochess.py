import random

plansza = [['k', 'k', 'k'], ['O', 'O', 'O'], ['g', 'g', 'g']]  # Początkowe ustawienie planszy
# Zmienne list wszystkich rodzajów pól (ich położenia zapisywanego za pomocą tuple (x,y))
lista_k = []
lista_o = []
lista_g = []


def wypisz_plansze():  # Wypisuje obecne ustawienie planszy w konsoli
    i = 0
    print('    0', '   1', '   2')
    for rzad in plansza:
        print(i, rzad)
        i += 1


def znajdz_pionki():  # Znajduje i zapisuje obecne ustawienie pionków na planszy
    global plansza, lista_g, lista_k
    # By szukać pionków zeruje listy, chyba da się to zrobić lepiej ale działa
    lista_g = []
    lista_k = []
    x = 0
    y = 0
    for rzad in plansza:  # Pętla znajdująca położenie wszystkich rodzajów pól
        for kolumna in rzad:
            if kolumna == 'g':
                # print('g: {}, {}'.format(x, y))
                lista_g.append((x, y))
            if kolumna == 'k':
                # print('k: {}, {}'.format(x, y))
                lista_k.append((x, y))
            if kolumna == 'O':
                # print('O: {}, {}'.format(x, y))
                lista_o.append((x, y))

            y += 1
        y = 0
        x += 1


def znajdz_ruch_g():  # Znajduje możliwe ruchy dla gracza
    global plansza, lista_pustych_g, lista_bic_g
    lista_pustych_g = []
    lista_bic_g = []
    for pionek in lista_g:  # Skomplikowana pętla znajdująca możliwe ruchy i bicia, try i except uważa by listy nie mogły loopować się do -1
        if plansza[pionek[0] - 1][pionek[1]] == 'O':
            lista_pustych_g.append(((pionek[0], pionek[1]), (pionek[0] - 1, pionek[1])))
            # print('puste', pionek[0], pionek[1])
        try:
            if pionek[0] - 1 == -1:
                raise IndexError
            if plansza[pionek[0] - 1][pionek[1] + 1] == 'k':
                # print('można bić', pionek[0], pionek[1])
                lista_bic_g.append(((pionek[0], pionek[1]), (pionek[0] - 1, pionek[1] + 1)))
        except IndexError:
            pass
        try:
            if pionek[1] - 1 == -1:
                raise IndexError
            if plansza[pionek[0] - 1][pionek[1] - 1] == 'k':
                # print('można bić', pionek[0], pionek[1])
                lista_bic_g.append(((pionek[0], pionek[1]), (pionek[0] - 1, pionek[1] - 1)))
        except IndexError:
            pass


def znajdz_ruch_k():  # Znajduje możliwe ruchy dla komputera
    global plansza, lista_pustych_k, lista_bic_k
    lista_pustych_k = []
    lista_bic_k = []
    for pionek in lista_k:
        if plansza[pionek[0] + 1][pionek[1]] == 'O':
            lista_pustych_k.append(((pionek[0], pionek[1]), (pionek[0] + 1, pionek[1])))
            # print('puste', pionek[0], pionek[1])
        try:

            if plansza[pionek[0] + 1][pionek[1] + 1] == 'g':
                # print('można bić', pionek[0], pionek[1])
                lista_bic_k.append(((pionek[0], pionek[1]), (pionek[0] + 1, pionek[1] + 1)))
        except IndexError:
            pass
        try:
            if pionek[1] - 1 == -1:
                raise IndexError
            if plansza[pionek[0] + 1][pionek[1] - 1] == 'g':
                # print('można bić', pionek[0], pionek[1])
                lista_bic_k.append(((pionek[0], pionek[1]), (pionek[0] + 1, pionek[1] - 1)))
        except IndexError:
            pass
    return lista_pustych_k + lista_bic_k


def ruch_g():  # Wyświetla możliwe ruchy z znajdz_ruch_g i pozwala na wybór któregoś z nich
    global plansza
    n = 1
    for ruch in lista_pustych_g:
        print(n, 'Pionek znajdujący się na polu {},{} może poruszyć się na pole {},{}'.format(ruch[0][0], ruch[0][1],
                                                                                              ruch[1][0], ruch[1][1]))
        n += 1
    for ruch in lista_bic_g:
        print(n, 'Pionek znajdujący się na polu {},{} może bić piona na polu {},{}'.format(ruch[0][0], ruch[0][1],
                                                                                           ruch[1][0], ruch[1][1]))
        n += 1
    lista_ruchow_g = lista_pustych_g + lista_bic_g
    # Win condition w wypadku braku możliwych ruchów
    if lista_ruchow_g == []:
        print('Komputer wygrał! Brak możliwych ruchów')
        exit()
    ruch_gracza = int(input('Podaj który ruch chcesz wykonać: '))
    wybrany_ruch = lista_ruchow_g[ruch_gracza - 1]
    print(wybrany_ruch)
    plansza[wybrany_ruch[0][0]][wybrany_ruch[0][1]] = 'O'
    plansza[wybrany_ruch[1][0]][wybrany_ruch[1][1]] = 'g'
    wypisz_plansze()


def ruch_k():  # Losuje ruch komputera z znajdz_ruchy_k
    try:
        global plansza
        lista_ruchow_k = lista_pustych_k + lista_bic_k
        # Win condition przy braku możliwych ruchów
        if lista_ruchow_k == []:
            print('Gracz wygrał! Brak możliwych ruchów')
            exit()
        ruch_k = lista_ruchow_k[random.randrange(0, len(lista_ruchow_k))]
        print(lista_ruchow_k)
        print(ruch_k)
        plansza[ruch_k[0][0]][ruch_k[0][1]] = 'O'
        plansza[ruch_k[1][0]][ruch_k[1][1]] = 'k'
        wypisz_plansze()
    except ValueError:
        print('brak możliwych ruchów')


def czy_koniec():  # Sprawdza czy gra się zakończyła - win condition
    global plansza
    ilosc_g = 0
    ilosc_k = 0
    # Wygrana gdy gracz doszedł do drógej strony planszy
    for kolumna in plansza[0]:
        if kolumna == 'g':
            print('Gracz wygrał! Dotarł do końca')
            exit()
    # Wygrana gdy komputer doszedł do drógej strony planszy
    for kolumna in plansza[2]:
        if kolumna == 'k':
            print('Komputer wygrał! Dotarł do końca')
            exit()
    # Wygrana gdy któryś z graczy zniszczył wszystkie piony przeciwnika
    for rzad in plansza:
        for kolumna in rzad:
            if kolumna == 'g':
                ilosc_g += 1
            elif kolumna == 'k':
                ilosc_k += 1
    if ilosc_g == 0:
        print('Komputer wygrał! Brak pionków przeciwnika')
    elif ilosc_k == 0:
        print('Gracz wygrał! Brak pionków przeciwnika')

# wypisz_plansze()
# znajdz_pionki()
# znajdz_ruch_g()
# znajdz_ruch_k()
# print(lista_o, lista_g, lista_k)
#
# print(lista_pustych_k, lista_pustych_g)
# print(lista_bic_k, lista_bic_g)
#
# ruch_g()
# ruch_k()
# wypisz_plansze()
# while True:  # Obecny substytut trwającej gry - wykonuje ww funkcje po kolei, TO DO: zmienić w funkcję
#     znajdz_pionki()
#     znajdz_ruch_g()
#     ruch_g()
#     czy_koniec()
#     znajdz_pionki()
#     znajdz_ruch_k()
#     ruch_k()
#     czy_koniec()


# wypisz_plansze()
# znajdz_pionki()
# znajdz_ruch_k()
# znajdz_ruch_g()
# ruch_g()
# znajdz_pionki()
# znajdz_ruch_k()
