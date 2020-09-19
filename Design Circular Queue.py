class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.front = 0
        self.rear = 0
        
        self.queue_size = 0     #for tracking size
        
        self.queue = [None] * k    #Created Queue with k size and left it empty 
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False
        else:
            self.queue[self.rear] = value
            
            self.rear = (self.rear + 1) % self.capacity     #tail should be modulus of total size
            
            self.queue_size += 1
            
            return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        else:
            self.front = (self.front + 1) % self.capacity
            self.queue_size -= 1
            
            return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty(): return -1
        else:
            return self.queue[self.front]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty(): return -1
        else:
            #here we do rear-1, because we update the rear pointer previously while performing enqueue operation.
            return self.queue[(self.rear-1)% self.capacity]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.queue_size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.queue_size == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

'''
#using lists
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.lst=[]
        self.size = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.lst)==self.size:
            return False
        self.lst.append(value)
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if not self.lst:
            return False
        
        self.lst.pop(0)
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if not self.lst: return -1
        return self.lst[0]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if not self.lst: return -1
        return self.lst[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if not self.lst:
            return True
        return False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if len(self.lst)==self.size:
            return True
        return False
'''