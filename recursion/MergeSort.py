class MergeSort:
    def __init__(self,max):
        self.theArray=[0]*max
        self.elements=0

    def _insert(self,var):
        self.theArray[self.elements]=var
        self.elements+=1

    def _display(self):
        for i in range(0,self.elements):
            print(str(self.theArray[i]))

    def _merge(self,workSpace,lowPtr,highPtr,upperBound):
        j=0
        lowerBound=lowPtr
        mid=highPtr-1
        n=(upperBound-lowerBound)+1

        while lowPtr<= mid and highPtr<= upperBound:
            if self.theArray[lowPtr]<self.theArray[highPtr]:
                workSpace[j]=self.theArray[lowPtr]
                j+=1
                lowPtr+=1
            else:
                workSpace[j]=self.theArray[highPtr]
                j+=1
                highPtr+=1

        while lowPtr<=mid:
            workSpace[j]=self.theArray[lowPtr]
            j+=1
            lowPtr+=1
        while highPtr<=upperBound:
            workSpace[j]=self.theArray[highPtr]
            j+=1
            highPtr+=1

        for i in range(0,n):
            self.theArray[lowerBound+i]=workSpace[i]

    def _reMergeSort(self,workSpace,lowerBound,upperBound):
        if lowerBound==upperBound:
            return
        else:
            mid=int((lowerBound+upperBound)/2)
            self._reMergeSort(workSpace,lowerBound,mid)
            self._reMergeSort(workSpace,mid+1,upperBound)
            self._merge(workSpace,lowerBound,mid+1,upperBound)

    def _MergeSort(self):
        workSpace = [0]*self.elements
        self._reMergeSort(workSpace,0,self.elements-1)

merge=MergeSort(15)
merge._insert(64)
merge._insert(21)
merge._insert(33)
merge._insert(70)
merge._insert(12)
merge._insert(85)
merge._insert(44)
merge._insert(3)
merge._insert(99)
merge._insert(0)
merge._insert(108)
merge._insert(36)

merge._MergeSort()
merge._display()


