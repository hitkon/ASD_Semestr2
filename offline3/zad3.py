import random

from zad3testy import runtests

# Ivan Zarzhitski
# Szukamy min początek i max koniec wśród przedziałow
# Używamy bucketSorta(na 50 przedziałów) na przedziale [min, max]
# W buketsorte używamy quicksort
# W najgorszem przypadkie złożoność będzie O(n**2), ale liczby są losowany zgodnie z rozkładem jednostajnym. Więc działa za O(n) ... w teorii.

def quickSort(tab):
    if len(tab) > 1:
        m=tab.pop()
        r, eq, l = [], [m], []
        for i in tab:
            if i == m:
                eq.append(i)
            elif i > m:
                r.append(i)
            else:
                l.append(i)
        return (quickSort(l) + eq + quickSort(r))
    else:
        return tab

def BucketSort(T, minD, maxD):
    podz = 50
    przed = (maxD - minD) / podz
    tab = [[] for _ in range(podz)]
    for i in T:
        tab[int((i - minD) / przed)].append(i)
    ans = []
    for i in range(podz):
        ans = ans + quickSort(tab[i])
    return ans


def SortTab(T,P):

    minD = P[0][0]
    maxD = P[0][1]
    for i in P:
        minD = min(minD, i[0])
        maxD = max(maxD, i[1])

    return BucketSort(T, minD, maxD)

    # tab = []
    # for i in P:
    #     if i[2] == 0:
    #         continue
    #     tab.append((i[0], 0))
    #     tab.append((i[1], 1))
    #
    # tab = sorted(tab)
    #
    # stack = []
    # res = []
    # for item in tab:
    #     if item[1] == 0:
    #         stack.append(item)
    #     else:
    #         if len(stack) == 1:
    #             buf = []
    #             minD = stack[0][0]
    #             maxD = item[0]
    #             for i in T:
    #                 if i >= minD and i <= maxD:
    #                     buf.append(i)
    #             res = res + BucketSort(buf, minD, maxD)
    #         stack.pop()
    # return res





if __name__ == "__main__":
    runtests( SortTab )