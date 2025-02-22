def binary_search(arr, low, high, key):
    if low <= high:
        mid = low + (high - low) // 2
        if key == arr[mid]:
            return mid
        if key < arr[mid]:
            return binary_search(arr, low, mid - 1, key)
        return binary_search(arr, mid + 1, high, key)
    return -1

arr = list(map(int, input().split()))
key = int(input())
arr.sort()
index = binary_search(arr, 0, len(arr) - 1, key)

if index != -1:
    print(f"{key}")
else:
    print("Not Found")
