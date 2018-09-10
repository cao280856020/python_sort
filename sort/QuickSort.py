array=[1,20,30,2,5,6,9,7,43,55,32,0,22,21,16]

def swap(i,j):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def manualSort(left,right,size):
    if size==1:
        return
    elif size==2:
        if array[left]>array[right]:
            swap(left,right)
    else:
        if array[left]>array[right]:
            swap(left,right)
        if array[left]>array[right-1]:
            swap(left,right-1)
        if array[right-1]>array[right]:
            swap(right-1,right)

def getPivot(left,right):
    center=(left+right)/2
    if array[left] > array[center]:
        swap(left, center)
    if array[left] > array[right]:
        swap(left, right)
    if array[center] > array[right]:
        swap(center, right)
    pivot=array[center]
    swap(center,right-1)
    return pivot

def getPartition(left,right,pivot):
    leftScan=left+1
    rightScan=right-2
    while True:
        while array[leftScan]<pivot:
            leftScan+=1
        while array[rightScan]>pivot:
            rightScan-=1

        if leftScan>=rightScan:
            break
        else:
            swap(leftScan,rightScan)
    swap(leftScan,right-1)
    return leftScan

def quickSort(left,right):
    size=right-left+1
    if size<=3:
        manualSort(left,right,size)
    else:
        pivot=getPivot(left,right)
        partition=getPartition(left,right,pivot)
        quickSort(left, partition-1)
        quickSort(partition+1, right)


quickSort(0,len(array)-1)
print(array)