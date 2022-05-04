from zad6testy import runtests

# Ivan Zarzhitski
# Robimy BFS od wierszchołka s z zapamiętywaniem dystansu do każdego wierszchołka.
# Zwrócimy najkrótszą scieżkę od s do t.
# Do wszystkich wierszhołków nie należących do ścieżki odznaczymy dystans równy +INF.
# Zaczynamy modyfikowany BFS po kolei po wierszhołkach ze ścieżki.
# Modyfikacja BFS w tym, że nie idziemy po krowiędziam, które należą do ścieżki.
# BFS zwraca największy(po długości od s) wierszchółek z scieżki, który da się osiągnąć inną ściężką za tu samu długość.
# Ta wartość będzie granicą, do której nie ma sensu usuwać krowiędź z ścieżki.
# Jeżeli dla jakiegoś wierszchołka nie będzie granicy, to usuwamy następną krawiędź w ścieżce.
# Jeżeli nie udało się usunąć krowiedź, to na koniec zwracamy None.
# Złożoność czasowa: O(n + m)
# Złożoność pamięciowa: O(n + m)
# WTF?! Dlaczego nie istnienie scieżki jest dłuższe niż istnienie ?????


def BFS(Graf, used, dist, start, start_dist = 0):
    queue = [start]
    used[start] = 1
    dist[start] = start_dist
    while len(queue) != 0:
        v = queue.pop(0)
        for to in Graf[v]:
            if used[to] == 0:
                used[to] = 1
                dist[to] = dist[v] + 1
                queue.append(to)

def BFS2(Graf, used, dist, start):
    barier = 0
    maxAchieved = 0
    queue = [start]
    while len(queue) != 0:
        v = queue.pop(0)
        for to in Graf[v]:
            if used[v] == 2 and used[to] == 2:
                continue

            if used[to] == 2:
                if dist[v] + 1 == dist[to]:
                    barier = max(barier, dist[to])
                else:
                    maxAchieved = max(maxAchieved, dist[to])
                continue

            if dist[to] > dist[v] + 1:
                dist[to] = dist[v] + 1
                queue.append(to)
    return (maxAchieved, barier)

def get_path_and_mark_it(Graf, dist, used, s, f):
    v = f
    used[f] = 2
    path = [f]
    while v != s:
        for to in Graf[v]:
            if dist[v] == dist[to] + 1:
                used[to] = 2
                path.append(to)
                v = to
                break
    return path[::-1]


def longer( G, s, t ):
    n = len(G)

    #Graf = [[] for _ in range(n)]

    # for g in G:
    #     Graf[g[0]].append(g[1])
    #     Graf[g[1]].append(g[0])

    Used = [0] * n
    Dist = [-1] * n

    BFS(G, Used, Dist, s)

    if Dist[t] == -1:
        return None

    path = get_path_and_mark_it(G, Dist, Used, s, t)
    print(path)

    #Used2 = [0] * n
    #Dist2 = [0] * n

    barier = 0
    maxAchievedVert = 0

    for i in range(n):
        if Used[i] != 2:
            Dist[i] = 10**9

    a = 1

    for i in range(len(path) - 1):
        v = path[i]
        result = BFS2(G, Used, Dist, v)
        maxAchievedVert = max(maxAchievedVert, result[0])
        barier = max(barier, result[1])
        if barier <= i:
            return (path[i], path[i+1])

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
if __name__ == "__main__":
    runtests( longer, all_tests = True )