arr = [6, 1, 9, 2, 1, 9]
n = 6

for i in range(n):
    for j in range(n-i-1):
        if arr[j] <= arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)