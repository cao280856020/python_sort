array=[1,20,30,2,5,6,9,7,43,55,32,0,22,21,16]

def swap(i,j):
    array[i],array[j]=array[j],array[i]

def selectSort():
    for out in range(0,len(array)-1):
        min=out
        for i in range(out+1,len(array)):
            if array[min]>array[i]:
                min=i;
        swap(min,out)


selectSort()
print(array)