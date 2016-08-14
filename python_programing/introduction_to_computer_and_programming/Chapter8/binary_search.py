def search(L, e):
    def bSearch(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)


print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5))
