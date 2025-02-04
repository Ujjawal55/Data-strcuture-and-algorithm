"""
problem is to sort the array using the (IBH) method.

"""


def positioned_x(arr, n, x):

    # two base condition
    if n == -1:
        arr.insert(0, x)
        return
    if arr[n] <= x:
        arr.insert(
            n + 1, x
        )  # insert the element on index right to the comparison which is important
        return

    # hypothesis step where we assume that the positioned_x will positioned the value at correct position for array size n - 1
    temp = arr.pop()
    positioned_x(arr, n - 1, x)

    # Induction step is to just append the final value to the array
    arr.append(temp)


def sort_arr(arr, n):  # this sort function return an sorted array upto the nth index

    # base condition
    if n == 0:
        return

    # hypothesis step: call the same method for n-1 objects and it will return a sorted array at index n - 1
    temp = arr.pop()
    # print(arr)
    sort_arr(arr, n - 1)

    # Induction step is that to put the nth element to the correct position in the above sorted array..
    # print(arr)
    positioned_x(arr, n - 1, temp)


def main():
    arr = [1, 0, 5, 3, -2, 15, 3]
    sort_arr(arr, len(arr) - 1)
    print(arr)


if __name__ == "__main__":
    main()
