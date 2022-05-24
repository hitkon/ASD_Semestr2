from zad8testy import runtests
import math

# Ivan Zarzhitski
# Budujemy listę wszystkich krawiędzi możliwych w grafie. Sortujemy według wartości.
# Idziemy po posortowanej liście i uruchamiamy algorytm Kruskała od każdej, pod warunkiem że ta krawędź będzie
# miała min wartość w podrzewie. Algorytm zwraca różnicę wartości pierwszej i ostatniej krawiędzi w poddrzewie.
# Wynikiem będzie min_wartość zwrócona algorytmem.
# Złożoność czasowa O(M * M * log N) = [ (M ~ N**2) ] = O(N**4 * log N)
# Złożoność pamięciowa: O(N**2)

def distance(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** (1/2)

def get(v, p):
    if v == p[v]:
        return v
    p[v] = get(p[v], p)
    return p[v]

def union(v, u, p, sizes):
    a = get(v, p)
    b = get(u, p)
    if sizes[a] < sizes[b]:
        a, b = b, a
    sizes[a] += sizes[b]
    p[b] = a

def Kruskal(G, start, n):
    p = [i for i in range(n)]
    sizes = [1 for i in range(n)]

    cnt = 0
    for i in range(start, len(G)):
        u, v, cost = G[i][1], G[i][2], G[i][0]
        if get(u, p) != get(v, p):
            cnt+=1
            union(u, v, p, sizes)
            if cnt == n-1:
                return (cost - G[start][0])
    return None


def highway( A ):
    G = []
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            dist = math.ceil(distance(A[i], A[j]))
            G.append((dist, i, j))
    G.sort()
    min_res = 10**9+7
    for i in range(len(G)):
        res = Kruskal(G, i, len(A))
        if res == None:
            break
        min_res = min(min_res, res)
    if min_res == 10**9+7:
        return None
    return min_res

# zmien all_tests na True zeby uruchomic wszystkie testy

runtests( highway, all_tests = True )