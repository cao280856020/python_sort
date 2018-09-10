import Heap as h

heap=h.Heap(8)
heap.insert(3);
heap.insert(27);
heap.insert(85);
heap.insert(93);
heap.insert(57);

size=input("size:")
for i in range(0,size):
    heap.insertAt(i,heap.remove())

heap.displayArray()

