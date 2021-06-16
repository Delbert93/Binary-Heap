
class Heap(object):
    binary_heap = []
    #test comment 
    def __init__(self, binary_heap = []):
        self._binary_heap = binary_heap

    def set_binary_heap(self, new_heap):
        self._binary_heap = new_heap
    

    def Push_To_Heap(self, number):
        self.binary_heap.append(number)
        #get index of our new member
        i = len(self.binary_heap)-1
        #bubble up
        done = False
        while(done != True and i != 1):
            if self.binary_heap[i] < self.binary_heap[i//2]:
                self.binary_heap[i], self.binary_heap[i//2] = self.binary_heap[i//2], self.binary_heap[i]
                i = i//2
            else:
                done = True
        pass

    def Pop_From_Heap(self):
        priority_item = self.binary_heap[1]
        self.binary_heap[1] = self.binary_heap[-1]
        self.binary_heap.pop()
        done = False
        i = 1
        #bubble down
        while(done != True and i*2+1 < len(self.binary_heap)):
            if self.binary_heap[i] > self.binary_heap[i*2] or self.binary_heap[i] > self.binary_heap[i*2+1]:
                if self.binary_heap[i*2] > self.binary_heap[i*2+1]:
                    self.binary_heap[i], self.binary_heap[i*2+1] = self.binary_heap[i*2+1], self.binary_heap[i]
                    i = i*2+1
                elif self.binary_heap[i*2+1] > self.binary_heap[i*2]:
                    self.binary_heap[i], self.binary_heap[i*2] = self.binary_heap[i*2], self.binary_heap[i]
                    i = i*2
            else:
                done = True
        if done != True:
            if i*2 > len(self.binary_heap):
                return priority_item
            elif self.binary_heap[i] > self.binary_heap[i*2]:
                self.binary_heap[i], self.binary_heap[i*2] = self.binary_heap[i*2], self.binary_heap[i]
        return priority_item

    def Peek_Heap(self):

        return self.binary_heap[1]



def test_bubble_down_and_peak_heap():
    heap = Heap()
    heap.binary_heap = [None, 1, 2, 4, 9, 10, 7]
    assert heap.Pop_From_Heap() == 1
    assert heap.Peek_Heap() == 2
    assert heap.binary_heap == [None, 2, 7, 4, 9, 10]
    assert len(heap.binary_heap)-1 == 5
    heap.Push_To_Heap(1)
    assert heap.Peek_Heap() == 1
