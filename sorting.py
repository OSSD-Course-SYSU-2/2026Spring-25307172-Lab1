def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    test_list = [3, 1, 4, 1, 5, 9, 2, 6]
    print("排序前:", test_list)
    sorted_list = bubble_sort(test_list)
    print("排序后:", sorted_list)