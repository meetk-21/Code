def bubble_sort(arr):

    n = len(arr)
    for i in range(n):
        swapped = False
        for y in range(0, n - i - 1): # it will swap until its in the order
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y] #swap if in wrong order
                swapped = True
        if not swapped:
            break
    return arr


# driver code
if __name__ == "__main__":
    dataset = [99, 45, 26, 5, 80, 58]
    print("Before:", dataset)
    sorted_dataset = bubble_sort(dataset)
    print("After:", sorted_dataset)
