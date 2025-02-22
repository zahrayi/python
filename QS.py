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


def QS(array, low, high):
    if low < high:
        s = sect(array, low, high)
        QS(array, low, s - 1)
        QS(array, s + 1, high)


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

    QS(array, 0, len(array) - 1)

    for i in range(len(array)):
        print(array[i], end=" ")
    print()
