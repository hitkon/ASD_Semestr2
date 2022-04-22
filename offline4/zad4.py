from zad4testy import runtests

# Ivan Zarzhitski
# Robę dynamikę dwuwymiarową, gdzie jeden wymiar to koszt, drugi to oś X.
# W elemencie z indeksami i j będziemy przechowywać maksymalną możliwą pojemność,
# którą możemy nabrać w [0, i] po X i spędzić nie więcej niż j Budżetu.
# Rozmiar tablicy będzie max(T[2])(maksymalny koniec), razy p + 1 (dodajemy wiersz z 0 budżetu).
# Sam algorytm.
# Dodajemy do każdego plana budynka indeks w tablicy T, i sortujemy plany po koncam odcinków.
# Uzupełniamy pierwszy wiersz i kolumnę zerami, to nasze warunki graniczne.
# Idziemy od najmniejszego końca do największego.
# Jak indeks kolumny wystąpi koniec bieżącego odcinka.
# Bedziemy iść po kolumnie od p do 0 i odnawiać znaczenie w dp[i][j] = max(poprzednego elementa w wierszu, i dp[j - T[i][3]][T[i][1] - 1] )
# Wynik zadania będzie w dp[p][max(T[2])].
# Dalej wracamy po tablicy odnawiamy budynki, którymi doszliśmy do tego wynika.
# Złożoność czasowa O(nlogn + np)
# Złożoność pamięciowa O(np)

def cmp(a):
    return a[2]

def Brutte(T, p):
    maxAns = []
    maxNumber = 0
    for z in range(1, 2**len(T)):
        ans = []
        Number = 0
        cost = 0
        j = z
        for i in range(len(T)):
            if j % 2 == 1:
                ans.append(i)
                Number+= T[i][0] * (T[i][2] - T[i][1])
                cost+= T[i][3]
            j//=2
        isCombination = True
        for i in range(len(ans)):
            for j in range(len(ans)):
                if i == j:
                    continue
                if((T[ans[i]][1] <= T[ans[j]][2] and T[ans[i]][1] >= T[ans[j]][1]) or (T[ans[i]][2] <= T[ans[j]][2] and T[ans[i]][2] >= T[ans[j]][1])):
                    isCombination = False
        if isCombination == True and cost <= p:
            if maxNumber < Number:
                maxAns = ans[:]
                maxNumber = Number
    return maxAns

def select_buildings(T,p):
    #return Brutte(T, p)
    buf_T = []
    for i in range(len(T)):
        buf_T.append((T[i][0], T[i][1], T[i][2], T[i][3], i))




    buf_T.sort(key=cmp)
    #print(buf_T)
    maxX = buf_T[-1][2]
    dp = [[-1 for _ in range(maxX + 1)] for _ in range(p + 1)]
    cur_buf = [0 for _ in range(p+1)]
    for i in range(p + 1):
        dp[i][0] = 0
    for i in range(maxX + 1):
        dp[0][i] = 0
    #print("HI")

    for i in range(len(buf_T)):
        for j in range(p, -1, -1):
            if i == 8:
                pass
            if buf_T[i][3] > j:
                break
            if dp[j - buf_T[i][3]][buf_T[i][1]-1] == -1:
                prev = 0
                for k in range(buf_T[i][1] - 1, -1, -1):
                    if(dp[j - buf_T[i][3]][k] != -1):
                        prev = dp[j - buf_T[i][3]][k]
                        break
                for k in range(buf_T[i][1] - 1, -1, -1):
                    if (dp[j - buf_T[i][3]][k] != -1):
                        break
                    else:
                        dp[j - buf_T[i][3]][k] = prev

            if dp[j][buf_T[i][2]] == -1:
                dp[j][buf_T[i][2]] = cur_buf[j]

            dp[j][buf_T[i][2]] = max(dp[j][buf_T[i][2]], dp[j - buf_T[i][3]][buf_T[i][1]-1] + (buf_T[i][0] * (buf_T[i][2] - buf_T[i][1])))
            cur_buf[j] = max(dp[j][buf_T[i][2]], cur_buf[j])

    ans = []
    # print(dp)
    # print(cur_buf)
    # for i in range(len(buf_T)):
    #print("Hi")

    p_buf = p
    x_state = maxX
    ind = len(buf_T)-1
    while dp[p_buf][x_state] != 0:
        if buf_T[ind][2] > x_state:
            ind-=1
            continue
        if buf_T[ind][2] < x_state:
            x_state = buf_T[ind][2]

        if p_buf >= buf_T[ind][3]:
            if dp[p_buf][buf_T[ind][2]] == buf_T[ind][0] * (buf_T[ind][2] - buf_T[ind][1]) + dp[p_buf - buf_T[ind][3]][buf_T[ind][1] - 1]:
                ans.append(buf_T[ind][4])
                x_state = buf_T[ind][1] - 1
                p_buf -= buf_T[ind][3]
        ind-=1
    print("HI")
    ans.sort()
    return ans

if __name__ == "__main__":
    runtests( select_buildings )