def linear_search(arr, x, count = 0):
    for i in range(len(arr)):
        count += 1
        if arr[i] == x:
            return i, count
        #return -1, count