def dutch_sort(i: int, arr: list):
    less, equal, greater = [], [], []
    for l in range(len(arr)):
        if arr[l] < arr[i]:
            less.append(arr[l])
        elif arr[l] > arr[i]:
            greater.append(arr[l])
        else:
            equal.append(arr[l])
    return less + equal + greater

def dutch_sort_2(i: int, arr: list):
    pivot = arr[i]
    smaller = 0
    for i in range(len(arr)):
        if arr[i] < pivot:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller += 1
    larger = len(arr) - 1
    for i in reversed(range(len(arr))):
        if arr[i] > pivot:
            arr[i], arr[larger] = arr[larger], arr[i]
            larger -= 1

def dutch_sort_3(i: int, arr: list):
    pivot = arr[i]
    less, equal, larger = 0, 0, len(arr) - 1
    while equal < larger:
        if arr[equal] < pivot:
            arr[less], arr[equal] = arr[equal], arr[less]
            equal, less = equal + 1, less + 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]
