def swap(array,i,j):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def bubbleSort(array):
    lastExchangeIndex=0
    sortEnding=len(array)-1
    for out in range(0,len(array)-1):
        isSorted=True
        for i in range(0,sortEnding):
            if array[i] > array[i+1]:
                swap(array,i,i+1)
                isSorted=False
                lastExchangeIndex=i
            i+=1
        if isSorted:
            break
        out+=1

array = [6,3,4,1,2,0,5,8,9]
bubbleSort(array)
print(array)