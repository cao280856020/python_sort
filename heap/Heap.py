import Node
class Heap:

    def __init__(self,max):
        self._currentSize=0
        self._maxSize=max
        self._heapArray=[0]*max

    def _isEmpty(self):
        return self._currentSize==0

    def _trickleUp(self,index):
        parentIndex=(index-1)/2
        bottom=self._heapArray[index]
        while index>0 and self._heapArray[parentIndex]._key<bottom._key:
            self._heapArray[index]=self._heapArray[parentIndex]
            index=parentIndex
            parentIndex=(parentIndex-1)/2
        self._heapArray[index] = bottom

    def insert(self,key):
        if self._currentSize>=self._maxSize:
            return False
        newNode=Node.Node(key)
        self._heapArray[self._currentSize]=newNode
        self._trickleUp(self._currentSize)
        self._currentSize += 1
        return True

    def _trickleDown(self,index):
        top=self._heapArray[index]
        largerIndex=0
        while index<self._currentSize/2:
            leftChild=index*2+1
            rightChild=leftChild+1
            if self._heapArray[leftChild]._key<self._heapArray[rightChild]._key:
                largerIndex=rightChild
            else:
                largerIndex=leftChild

            if top._key>=self._heapArray[largerIndex]._key:
                break

            self._heapArray[index]=self._heapArray[largerIndex]
            index=largerIndex

        self._heapArray[index]=top

    def remove(self):
        root=self._heapArray[0]
        self._currentSize-=1;
        self._heapArray[0]=self._heapArray[self._currentSize]
        self._trickleDown(0)
        return root

    def change(self,index,newValue):
        if index<0 or index>self._currentSize:
            return False

        oldValue=self._heapArray[index]._key
        self._heapArray[index]._key=newValue
        if oldValue<newValue:
            self._trickleUp(index)
        else:
            self._trickleDown(index)

        return True

    def displayArray(self):
        for j in range(0,self._maxSize):
            if self._heapArray[j]!=0:
                print(self._heapArray[j]._key)
            else:
                print(0)
    def insertAt(self,index,newNode):
        self._heapArray[index]=newNode