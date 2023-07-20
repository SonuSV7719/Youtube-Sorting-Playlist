arr = [2,6,1,8,3]
n = 5


for i in range(n-1):
    for j in range(i, n):
        if (arr[i] > arr[j]):
            arr[i], arr[j] = arr[j], arr[i]


# for i in range(n-1):
#     min = i
#     for j in range(i, n):
#         if (arr[i] > arr[j]):
#             min = j
#     arr[i], arr[min] = arr[min], arr[i]

print(arr)