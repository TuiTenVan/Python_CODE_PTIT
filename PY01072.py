def find_combinations(arr, n, k):
    while arr[0] <= n - k + 1:
        for i in range(0, k):
            print(arr[i], end=" ")
        print()
        j = k - 1
        while j >= 0 and arr[j] == n - k + j + 1:
            j -= 1
        if j >= 0:
            arr[j] += 1
            for t in range(j + 1, k):
                arr[t] = arr[t - 1] + 1
        else:
            break    

n, k = map(int, input().split()) 
a = list(map(int, input().split()))
ar = set(a)
arr = list(ar)
find_combinations(arr, len(arr), k)
