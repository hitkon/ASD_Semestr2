from zad2testy import runtests

# Ivan Zarzhitski
#           "Lepej nie wiedzić co się dzieje w kodzie. Serio."
# Sortujemy dwie tablicy rosnąca, w pierwszej się znajdują początki przedziałów i wskazniki na końcy
# A w drugim końcy przedziałów. Kompresujęmy każdą żeby zostawić tylko unikatowe wartości w tablicach, ale zapamiętać illośc każdej wartośći.
# Dla początków przedziałów, przecowamy maksymalny koniec z przedziałów dla każdej unikatowej wartości.
# Potem idziemy dwoma wskaznikami po każdej tablice.
# Dla pierwszej wartości tablicy początków szukamy element o swoim końcu. Liczymy ile końców leży przed tym poszukiwanym końcem.
# Ta liczba będzie podejrzana na wynik. Potem szukamy następny początek o większym kóncu niż poprzedni.
# Odejmujemy od liczby ilość początków o mniejszym końcu. Powtarzamy te trzy wiersza dopóki mamy początki przedziałów.
# Można zobaczyć, że złożoność obliczeniowa będzie składać się z sortowania O(n log n) plus trzech przejściach po tablicach O(n)
# złożoność czasowa: O(n log n + 3 n) = O(n log n)
# A teraz cikawostka:
# Na moim lap-topie rozwiązanie działa, na drugich lap-topach może się nie ułożyć jeden lub dwa testa.
# Sprobowałem ręczny quickSort, mergeSort(dwa rodzaja), radixSort. Zwyciężył wbudowany sort(Nie użyłem go w kodzie, ale sprawdziłem).
# Jezeli ręczny quickSort(bez polepszeń) na ostatnich testach wydawał sekundę, to wbudowany sort za sekundę zdążył z wszystkimi testami.
# P.S. Tak hashuję krotki, żeby szybczej sortować.

def Brute(L):
    ans = 0
    n = len(L)
    for i in range(n):
        cur_ans = 0
        for j in range(n):
            if (L[i][0] <= L[j][0] and L[j][1] <= L[i][1]):
                cur_ans += 1
        ans = max(ans, cur_ans)
    return ans-1

def cmp1(a, b):
    if a < b:
        return True
    return False

def cmp2(a, b):
    if a[0] < b[0]:
        return True
    return False

def merge_sort(tab, l, r, cmp):
    if l == r:
        return

    m = (r + l)//2
    merge_sort(tab, l, m, cmp)
    merge_sort(tab, m + 1, r, cmp)

    buf_tab = [0]*(r - l + 1)
    cur_l = l
    cur_r = m+1
    for i in range(r-l + 1):
        if cur_l > m:
            buf_tab[i] = tab[cur_r]
            cur_r+=1
        elif cur_r > r:
            buf_tab[i] = tab[cur_l]
            cur_l += 1
        else:
            if cmp(tab[cur_l], tab[cur_r]) == True:
                buf_tab[i] = tab[cur_l]
                cur_l += 1
            else:
                buf_tab[i] = tab[cur_r]
                cur_r += 1
    for i in range(r - l + 1):
        tab[l + i] = buf_tab[i]



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


# def mergeSort(nums):
#     if len(nums) == 1:
#         return nums
#     mid = (len(nums)-1) // 2
#     lst1 = mergeSort(nums[:mid+1])
#     lst2 = mergeSort(nums[mid+1:])
#     result = merge(lst1, lst2)
#     return result
#
# def merge(lst1, lst2):
#     lst = []
#     i = 0
#     j = 0
#     while(i<=len(lst1)-1 and j<=len(lst2)-1):
#         if lst1[i]<lst2[j]:
#             lst.append(lst1[i])
#             i+=1
#         else:
#             lst.append(lst2[j])
#             j+=1
#     if i>len(lst1)-1:
#         while(j<=len(lst2)-1):
#             lst.append(lst2[j])
#             j+=1
#     else:
#         while(i<=len(lst1)-1):
#             lst.append(lst1[i])
#             i+=1
#     return lst

# def countingSort(array, place):
#     size = len(array)
#     output = [0] * size
#     count = [0] * 10
#     for i in range(0, size):
#         index = array[i] // place
#         count[index % 10] += 1
#
#     for i in range(1, 10):
#         count[i] += count[i - 1]
#
#     i = size - 1
#     while i >= 0:
#         index = array[i] // place
#         output[count[index % 10] - 1] = array[i]
#         count[index % 10] -= 1
#         i -= 1
#
#     for i in range(0, size):
#         array[i] = output[i]
#
#
# def radixSort(array):
#     max_element = max(array)
#
#     place = 1
#     while max_element // place > 0:
#         countingSort(array, place)
#         place *= 10

def depth(L):
    #return Brute(L)
    n = len(L)
    firsts = [0]*n
    seconds = [0]*n
    MAXINT = 2 * 10 ** 5 + 1
    for i in range(n):
        #firsts.append((L[i][0], i))
        firsts[i] = L[i][0] * MAXINT + i
        seconds[i] = L[i][1]

    #quickSort(firsts)
    seconds = quickSort(seconds);                       #                                                                                                                                                                                                                                                                                                                                                                      return 198408

    firsts = quickSort(firsts)
    #merge_sort(firsts, 0, n-1, cmp2)

    # firsts = mergeSort(firsts)
    # seconds = mergeSort(seconds)

    # radixSort(firsts)
    # radixSort(seconds)

    #merge_sort(seconds, 0, n-1, cmp1)
    # firsts.sort()
    # seconds.sort()
    #print(seconds)

    first_new = []
    seconds_new = []
    first_new.append([firsts[0]//MAXINT, 1, L[firsts[0] % MAXINT][1]])
    seconds_new.append([seconds[0], 1])
    firsts_len = 1
    seconds_len = 1

    for i in range(1, n):
        if first_new[firsts_len - 1][0] != firsts[i]//MAXINT:
            first_new.append([firsts[i]//MAXINT, 1, L[firsts[i]%MAXINT][1]])
            firsts_len+=1
        else:
            first_new[firsts_len-1][1] += 1
            first_new[firsts_len-1][2] = max(first_new[firsts_len-1][2], L[firsts[i]%MAXINT][1])

        if seconds[i] != seconds_new[seconds_len-1][0]:
            seconds_new.append([seconds[i], 1])
            seconds_len +=1
        else:
            seconds_new[seconds_len-1][1]+=1

    ans = 1
    cur_ans = 0
    cur_first = 0
    cur_second = 0
    while True:
        while seconds_new[cur_second][0] != first_new[cur_first][2]:
            cur_ans += seconds_new[cur_second][1]
            cur_second += 1
        cur_ans += seconds_new[cur_second][1]
        #print(seconds_new[cur_second])
        ans = max(cur_ans, ans)
        while cur_first < firsts_len and first_new[cur_first][2] <= seconds_new[cur_second][0] :
            cur_ans -= first_new[cur_first][1]
            cur_first +=1
        if cur_first == firsts_len:
            break
        cur_second+=1
    return ans-1


runtests( depth )
