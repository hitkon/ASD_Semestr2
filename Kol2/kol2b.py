from kol2btesty import runtests

# Ivan Zarzhitski
# Sortujemy po odleglości.
# I rekurencyjnie idziemy rec (i, is_shift) = min(j, is_shift) + C[j], distance < T, j < i, i używamy raz shift jeżeli go mamy.
# rec = min(i, 1) = (min(j, 0) + C[j], i > j, 2*T>=dist > T )
# Złożoność czasowa O(n log n + n * T)
# Złożoność pamięciowa O(n)

def rec(x, ind, min_cost_tab, is_shift, buf_tab, C, T):
    if (is_shift == 1 and x <= 2 * T) or (is_shift == 0 and x <= T):
        return 0

    if min_cost_tab[is_shift][ind] == -1:
        min_cost_ind = 10 ** 9
        for i in range(ind-1, -1, -1):
            dist = (buf_tab[ind][0] - buf_tab[i][0])
            if (is_shift == 1 and dist > 2 * T) or (is_shift == 0 and dist > T):
                break
            if dist <= T:
                min_cost_ind = min(min_cost_ind, rec(buf_tab[i][0], i, min_cost_tab, is_shift, buf_tab, C, T) + C[buf_tab[i][1]])
            else:
                min_cost_ind = min(min_cost_ind, rec(buf_tab[i][0], i, min_cost_tab, 0, buf_tab, C, T) + C[buf_tab[i][1]])
        min_cost_tab[is_shift][ind] = min_cost_ind
    return min_cost_tab[is_shift][ind]

def Brutte( O, C, T, L):
    O.append(L)
    C.append(0)

    buf_tab = [(O[i], i) for i in range(len(O))]
    buf_tab.sort()
    min_cost_tab_without_shift = [-1 for _ in range(len(O))]
    min_cost_tab_with_shift = [-1 for _ in range(len(O))]
    min_cost_tab = [min_cost_tab_without_shift, min_cost_tab_with_shift]

    # return -1

    #print(min_cost_tab)
    return rec(L, len(O) - 1, min_cost_tab, 1, buf_tab, C, T)

def build_tree(tree, v, l, r,  tl, tr, tab):
    if l == tl and r == tr:
        tree[v] = tab[l]
        return tree[v]
    m = (l + r) // 2


def min_cost( O, C, T, L ):
    INF = 10**9


# zmien all_tests na True zeby uruchomic wszystkie testy

runtests( min_cost, all_tests = True )
