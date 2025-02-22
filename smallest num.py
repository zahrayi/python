def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def sect(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            swap(array, i, j)
    swap(array, i + 1, high)
    return i + 1


def quick_select(array, low, high, k):
    if low <= high:
        s = sect(array, low, high)
        if s == k:
            return array[s]
        elif s > k:
            return quick_select(array, low, s - 1, k)
        else:
            return quick_select(array, s + 1, high, k)


if __name__ == "__main__":
    input_line = input()
    array = []

    num = ""
    for char in input_line:
        if char == " ":
            if num != "":
                array.append(int(num))
                num = ""
        else:
            num += char
    if num != "":
        array.append(int(num))

    k = int(input()) - 1  # به صفر ایندکس تبدیل می‌کنیم

    result = quick_select(array, 0, len(array) - 1, k)
    print(result)
