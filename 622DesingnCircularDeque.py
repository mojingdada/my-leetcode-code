class MyCircularQueue(object):
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.item=[]
        self.k=k

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if(len(self.item)>=self.k):
            return False
        else:
            self.item.append(value)
            return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if(len(self.item)==0):
            return False
        else:
            self.item.pop()
            return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if (len(self.item)==0):
            return -1
        else:
            return self.item[0]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if (len(self.item)==0):
            return -1
        else:
            return self.item[-1]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if(len(self.item)==0):
            return True

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if(len(self.item)>=0):
            return True




if __name__ == '__main__':
    item=MyCircularQueue(k=3)
    print(MyCircularQueue.enQueue(item,1))
