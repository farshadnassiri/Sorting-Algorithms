from sys import builtin_module_names


def bubble_sort(list):
    n=len(list)
    for i in range(n):
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list                    
                
if __name__  == "__main__":
    assert bubble_sort([3,2,1]) == [1,2,3]
  