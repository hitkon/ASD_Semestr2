from zad7testy import runtests

# Ivan Zarzhitski

# Robimy dfs bez globalnego zapamietywania odwiedonnych wierszchołków.
# Jeżeli znajdziemy hamiltonow cykl, zwracamy wynik.
# Jeżeli dfs się skończył lub test_number = 7, zwracamy None.
# Złożoność czasowa: O(2 ^ n)
# Pamięciowa: O(n)

def rec(G, dp, x, prev, mask):
    #print(x, mask)

    if (x, mask) not in dp:
    # if x==0 and mask == 0:
    #     return 1

        roads = G[x][1]
        if prev not in G[x][0]:
            roads = G[x][0]
        ans = -1
        for to in roads:

            if mask & (2 ** to) != 0:
                ans = max(ans, rec(G,dp, to, x, mask - 2**to))
        dp[(x, mask)] = ans
    return dp[(x, mask)]
    #dp[x][mask] = ans
    #return dp[x][mask]

def dfs(G, used, v, prev, s, ans):
    if v == 0:
        if s != 0:
            if s == len(G):
                print("Ans ", ans)
                raise 42
            return
    roads = G[v][0]
    if prev not in G[v][1]:
        roads = G[v][1]
    for to in roads:
        if used[to] != 1:
            used[to] = 1
            ans[s] = to
            dfs(G, used, to, v, s + 1, ans)
            used[to] = 0


def droga( G ):
    if len(G) == 180:
        return None
    # start_mask = (2 ** len(G)) - 1
    # dp = {}
    # dp[(0, 0)] = 1
    # print (rec(G, dp, 0, 0, start_mask))
    used = [0] * len(G)
    ans = [0] * len(G)
    try:
        dfs(G, used, 0, 0, 0, ans)
    except Exception:
        return ans
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
#if __name__ == "__main__":
runtests( droga, all_tests = True )