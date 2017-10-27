# insertion sort
def insertionSort(my_List):
    for j in range(2,len(my_List)):
        key = my_List[j]
        i = j-1
        while i > 0 and my_List[i]>key:
            my_List[i+1]=my_List[i]
            i=i-1
        my_List[i+1]=key
