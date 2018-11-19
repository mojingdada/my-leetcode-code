class Tirednode:
    def __init__(self,x):
        self.val=x
        self.children=[None for _ in range(26)]
        self.isEnd=False
    def insertStr(self,dict,root):
        for ch in list(dict):
            pos=ord(ch)-ord('a')
            if(root.children[pos]==None):
                root.children[pos]=Tirednode(ch)
            else:
                pass

            root=root.children[pos]
        root.isEnd=True

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        root = Tirednode(None)
        for word in range(0, len(dict)):
            Tirednode.insertStr(root, dict[word], root)
        str1=sentence.split(" ")
        for i in range(0,len(str1)):
            res=""
            node=root
            for j in range(0,len(str1[i])):
                pos=ord(str1[i][j])-ord('a')
                if(node.children[pos]!=None):
                    res+=node.children[pos].val
                    node = node.children[pos]
                else:
                    break
                if(node.isEnd==True):
                    str1[i]=res
                    break;
        return " ".join(str1)
    if __name__ == '__main__':
        dict = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        newsentence=replaceWords(dict,dict,sentence)
        print(newsentence)



