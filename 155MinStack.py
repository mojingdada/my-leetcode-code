class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.item=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.item.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.item.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.item[-1]

    def getMin(self):
        """
        :rtype: int
        """
        x = self.item[:]
        x.sort()
        return x[0]




        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()