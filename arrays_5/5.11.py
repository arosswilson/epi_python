def next_perm(arr: list):
    next_perm_found = False
    for i in reversed(range(1, len(arr))):
        if arr[i] > arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            next_perm_found = True
            break
    if not next_perm_found:
        return []
    for j in range(i, len(arr)-1):
        arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(next_perm([1,2,3,1]))
print(next_perm([2,2,4,1,3]))
