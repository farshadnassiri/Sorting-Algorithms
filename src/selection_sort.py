


def selection_sort(list: List[int]) -> List[int]:
   
    for i in range(len(list)):
        min_idx = i
        for j in range(i + 1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list

if __name__ == "__main__":
    assert selection_sort([3, 1, 2]) == [1, 2, 3]
