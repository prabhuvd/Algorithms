'''

Weighted quick-union.
-Modify quick-union to avoid tall trees.
-Keep track of size of each component.
-Balance by linking small tree below large one.

https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf

Created on Dec 28, 2016

@author: pdesai 
'''

class QUnionImprove:   
    def __init__(self,length=10):
        self.__quimpNodes=[]
        self.__quiBlockedNodes=[]  
        self.__quiNodeSize=[]        
        for arrIndex in range(length*length):    
            self.__quimpNodes.append(arrIndex)
            self.__quiBlockedNodes.append(0)   
            self.__quiNodeSize.append(1)     

    def setBlockedSite(self,index):
        self.__quiBlockedNodes[index] = 1

    def getBlockedSite(self,index):
        return self.__quiBlockedNodes[index]
    
    def getQUImpData(self):
        return self.__quimpNodes
            
    def root(self,node):        
        while(node != self.__quimpNodes[node]):
            node= self.__quimpNodes[node]
        return node
    
    def connected(self,node_a , node_b):
        if(self.root(node_a) == self.root(node_b)):        
            return True
        else:
            return False        
    
    def union(self,node_a,node_b):
        #print "Union (",node_a,node_b,")"
        root_of_node_a = self.root(node_a)
        root_of_node_b = self.root(node_b)
        if(self.__quiNodeSize[node_a]<self.__quiNodeSize[node_b]):
            self.__quimpNodes[root_of_node_a] = root_of_node_b
            self.__quiNodeSize[root_of_node_b] =self.__quiNodeSize[root_of_node_b]+1
             
        else:
            self.__quimpNodes[root_of_node_b] = root_of_node_a
            self.__quiNodeSize[root_of_node_a] =self.__quiNodeSize[root_of_node_a]+1 
            
        #print self.__quimpNodes   
        #print self.__quiNodeSize

        
# x = QUnionImprove(10)
# print x.__quimpNodes
# print x.__quiNodeSize
# 
# x.union(4,3)
# 
# print x.connected(3, 4)
# print x.root(3)
# print x.root(4)
# 
# x.union(3,8)
# x.union(6,5)
# x.union(9,4)
# x.union(2,1)
#  
# 
# print x.connected(1,7)
# 
# x.union(5,0)
# x.union(7,2)
# x.union(6,1)
# x.union(7,3)

