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

def build_tree(tree, v, l, r, tab):
    if l == r:
        tree[v] = tab[l]
    else:
        m = (l + r) // 2
        build_tree(tree, v * 2, l, m, tab)
        build_tree(tree, v * 2 + 1, m+1, r, tab)
        tree[v] = min(tree[v* 2], tree[v*2+1])

def get_min(tree, v, l, r, tl, tr, tab):
    if l == tl and r == tr:
        return tree[v]
    else:
        m = (l + r) // 2
        ans = 10**9
        if tl <= m:
            ans = min(ans, get_min(tree, v * 2, l, m, tl, m))
        if tr > m:
            ans = min(ans, get_min(tree, v * 2 + 1, m + 1, r, m+1, tr))
        return ans


def update_min(tree, v, l, r, ind, elem):
    if l == r:
        tree[v] = elem
    else:
        m = (l + r) //2
        if ind <= m:
            update_min(tree, v*2, l, m, ind, elem)
        else:
            update_min(tree, v * 2 + 1, m+1, r, ind, elem)
        tree[v] = min(tree[v* 2], tree[v*2+1])

def Heapify(heap, n, i):
    while i * 2 + 1 < n:
        l = i * 2 + 1
        r = i * 2 + 2
        min_ind = l

        if r < n and heap[r] < heap[l]:
            min_ind = r

        if heap[i] <= heap[min_ind] :
            break
        heap[i], heap[min_ind] = heap[min_ind], heap[i]
        i = min_ind

def build_heap(heap, n):
    for i in range(n //2, -1, -1):
        Heapify(heap, n, i)


def min_cost( O, C, T, L ):
    O.append(L)
    C.append(0)
    buf_tab = [(O[i], i) for i in range(len(O))]
    buf_tab.append((0, 0))
    buf_tab.sort()

    min_to_left_side = [10**9 for i in range(len(buf_tab))]
    min_to_right_side = [10 ** 9 for i in range(len(buf_tab))]

    n = len(buf_tab)

    min_to_right_side[len(buf_tab) -1] = 0
    min_to_left_side[0] = 0
    left_tree = [(len(buf_tab)+1)*4]
    right_tree = [(len(buf_tab)+1)*4]

    # build_tree(left_tree, 1, 0, n-1, min_to_left_side)
    # build_tree(right_tree, 1, 0, n-1, min_to_right_side)






# zmien all_tests na True zeby uruchomic wszystkie testy
if __name__ == "__main__":
    runtests( min_cost, all_tests = True )
