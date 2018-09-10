array = [6,3,4,1,2,0,5,8,9]

def shellSort():
    h=1;
    while h<=len(array):
        h=3*h+1

    while h>0:
        for out in range(h,len(array)):
            temp=array[out]
            i=out
            while i>h-1 and array[i-h]>temp:
                array[i]=array[i-h]
                i-=h
            array[i]=temp
        h=(h-1)/3

shellSort()
print(array)