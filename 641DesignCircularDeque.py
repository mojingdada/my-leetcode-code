class MyCircularDeque(object):
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.item=[]
        self.k=k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if(len(self.item)>=self.k):
            return False
        else:
           self.item.insert(0,value)
           return True
    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if(len(self.item)>=self.k):
            return False
        else:
            self.item.insert(-1,value)
            return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if(len(self.item)==0):
            return False
        else:
            self.item.pop(0)
            return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if (len(self.item) == 0):
            return False
        else:
            self.item.pop(-1)
            return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if (len(self.item) == 0):
            return -1
        else:
            return self.item[0]


    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if (len(self.item) == 0):
            return -1
        else:
            return self.item[-1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if (len(self.item) == 0):
            return True
        else:
            return False

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if (len(self.item) >= self.k):
            return True
        else:
            return False

