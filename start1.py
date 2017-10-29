# insertion sort
def insertion_sort(my_List):
    for j in range(1,len(my_List)):
        key = my_List[j]
        i = j-1
        while i > -1 and my_List[i]>key:
            my_List[i+1]=my_List[i]
            i=i-1
        my_List[i+1]=key
    print(my_List)

def find_value(my_List, value):
    values_List = []
    for j in range(len(my_List)):
        if my_List[j] == value:
            values_List.append(j)
    print values_List

# def add_binary(first, second):
#     sum=[]
#     if len(first) < len(second):
#         for i in (len(second)-len(first)):
#             first.insert(0,0)
#     if len(second) < len(first):
#         for i in (len(first)-len(second)):
#             second.insert(0,0)
#     for j in range(len(first))
#         s = first[len(first)-j]+second[len(first)-j]
#             if s

def selection_sort(my_List):
    for i in range(len(my_List)):
        key = my_List[i]
        print key
        smallest = [key, i]
        for j in range(i, len(my_List)):
            if my_List[j] < smallest[0]:
                smallest=[my_List[j], j]
        print smallest
        my_List[i]=smallest[0]
        my_List[smallest[1]]=key
        print my_List
    print my_List
