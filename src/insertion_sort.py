
def insertion_sort(list):
    
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list

if __name__ == "__main__":
    assert insertion_sort([3, 1, 2]) == [1, 2, 3]
