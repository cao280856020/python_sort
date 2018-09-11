class StackX:

    SIZE=20

    def __init__(self):
        self.top=-1
        self.array=[0]*self.SIZE

    def _peek(self):
        return self.array[self.top]

    def _pop(self):
        if self.top == -1:
            return False
        temp=self.array[self.top]
        self.top-=1
        return temp

    def _push(self,key):
        self.top+=1
        if self.top==self.SIZE:
            return False
        self.array[self.top]=key
        return True

    def _isEmpty(self):
        return self.top==-1