from kol1atesty import runtests

# Ivan Zarzhitski
# Przepraszam nie wiem, jak przetłumaczyć "Бор", niby łas, ale odznaczę jak BOR
# W BORZE (oprócz BORA) przechowywamy ilość stringów, która koncze się w tym miejscu
# Każdy string obracamy.
# Jeżeli string nie jest polindromem, to dokładamy dwa stringa do BORu.
# Jeżeli string jest polindromem to tylko jeden string kladziemy.
# Funkcja dokladania powiększa nam w jakimś elemencie koncówkę i zwraca ile stringów tam już się skończyło.
# Złożoność czasowa i pamięciowa: O(N) (Nawet lepiej niż O(N + n log n) :) Zerowy próg złożoności )


def add_to_bor(s, bor):
    pos = 0
    for i in range(len(s)):
        ch = ord(s[i]) - 97
        if bor[pos][ch + 1] == -1:
            bor.append([-1] * 27)
            bor[pos][ch + 1] = len(bor)-1
        pos = bor[pos][ch+1]
    bor[pos][0] += 1
    return bor[pos][0]


def g(T):
    bor = [[-1] * 27]
    res = -1
    for i in T:
        rev_i = i[::-1]
        buf = add_to_bor(i, bor)
        if buf > res: # można użyć max, ale nie pamiętam czy możliwie
            res = buf
        if i != rev_i:
            add_to_bor(rev_i, bor)
    return res + 1


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True)
