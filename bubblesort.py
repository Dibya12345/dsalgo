def swap(i, j, array):
    array[i], array[j]= array[j], array[i]
def bubblesort(array):
    isSorted=False
    while not isSorted:
        isSorted=True
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                swap(i, i+1, array)
                print(str(i)+" "+"sort"+"="+str(array)) 
                isSorted=False
    return array
array=[8,5,2,9,5,6,3]
print(bubblesort(array)) # [8,5,2,9,5,6,3]
