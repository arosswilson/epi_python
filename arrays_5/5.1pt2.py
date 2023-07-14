def dutch_flag(i: int, arr: list):
    pivot = arr[i]
    smaller = 0
    for i in range(len(arr)):
        if arr[i] < pivot:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller += 1
        print(arr)
    larger = len(arr) - 1
    for i in reversed(range(len(arr))):
        if arr[i] > pivot:
            arr[i], arr[larger] = arr[larger], arr[i]
            larger -= 1
        print(arr)

dutch_flag(3, [0,1,2,0,2,1,1])