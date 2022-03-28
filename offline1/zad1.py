from zad1testy import Node, runtests
# Ivan Zarzhitski
# Dwa przypadki
# Jeżeli k <= 5 użyjemy k razy wewnętrzną pętlę bubble sort(na liście), zauważymy, że tak można posortować K-chaotic listu
# Inaczej stworzymy heap(min_heap) na okience w pierwszych (k+1) elementów(robimy kopieję do k+1-elementowej tablicy).
# Dostajemy minimum, dodajemy do końca posortowanej listy i dodajemy następny (k+2)-element.
# Jakby Przesujemy okno na jeden element w prawo.
# Tak robimy dopóki możemy przesuwać okno. Na końcu (jak nie potrafimy dalej przesunąć k+1-elementowe okno)
# robimy heap_sort dodawając do końca posortowanej listy elementy po koleje.

# Złożoność czasowa algorytma
# k = 1 => O(n * k) = O(n)
# k = log(n) => O(n * log k)
# k = n => O(n * log k) = O(n * log n)

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

def list_len(p):
    cnt = 0
    k = p
    while k is not None:
        cnt+=1
        k = k.next
    return cnt

def Bubble_sort(p, k, n):
    first = p
    for i in range(k):
        l = first
        r = l.next
        if l.val > r.val:
            first = r
            r.next, l.next = l, r.next

        cur = first
        while cur.next.next is not None:
            l = cur.next
            r = l.next
            if l.val > r.val:
                cur.next = r
                r.next, l.next = l, r.next
            cur = cur.next
    return first

def merge_sort(head1, head2):
    head1_cpy = head1
    head2_cpy = head2
    sorted_head = None
    sorted_cur = None

    if head1_cpy.val < head2_cpy.val:
        sorted_head = head1
        head1_cpy = head1_cpy.next
    else:
        sorted_head = head2
        head2_cpy = head2_cpy.next
    sorted_cur = sorted_head

    while head1_cpy is not None and head2_cpy is not None:
        if (head1_cpy.val < head2_cpy.val):
            sorted_cur.next = head1_cpy
            head1_cpy = head1_cpy.next
        else:
            sorted_cur.next = head2_cpy
            head2_cpy = head2_cpy.next
        sorted_cur = sorted_cur.next

    if head1_cpy is not None:
        sorted_cur.next = head1_cpy
    if head2_cpy is not None:
        sorted_cur.next = head2_cpy

    return sorted_head

def merge_rec(p, n):
    if n == 1:
        return p
    m = n // 2
    head1 = p
    tail1 = p
    for i in range(m-1):
        tail1 = tail1.next
    head2 = tail1.next
    tail1.next = None
    head1 = merge_rec(head1, m)
    head2 = merge_rec(head2, n - m)
    return merge_sort(head1, head2)

def SortH(p,k):
    n = list_len(p)
    if n <= 1 or k == 0:
        return p

    return merge_rec(p, n)

    if k <= 5:
        return Bubble_sort(p,k,n)

    if k >= n - 1:
        k = n - 1
    k += 1

    heap = [0] * k
    p_cpy = p
    for i in range(k):
        heap[i] = p_cpy.val
        p_cpy = p_cpy.next

    build_heap(heap, k)

    sorted_list = Node()
    sorted_list_last = sorted_list


    while p_cpy is not None:
        sorted_list_last.val = heap[0]
        heap[0] = p_cpy.val
        p_cpy = p_cpy.next
        Heapify(heap, k, 0)
        sorted_list_last.next = Node()
        sorted_list_last = sorted_list_last.next

    for i in range(k-1):
        sorted_list_last.val = heap[0]
        sorted_list_last.next = Node()
        sorted_list_last = sorted_list_last.next
        heap[0], heap[k-1-i] = heap[k-1-i], heap[0]
        Heapify(heap, k - i - 1, 0)

    sorted_list_last.val = heap[0]

    return sorted_list



runtests( SortH )
