def ShellSort(arr):
    l = len(arr)
    gap = l//2
    swapped = False

    while gap != 1 or swapped:
        for i in range(gap, l):
            if arr[i-gap] > arr[i]:
                temp = arr[i]
                arr[i] = arr[i-gap]
                arr[i-gap] = temp
