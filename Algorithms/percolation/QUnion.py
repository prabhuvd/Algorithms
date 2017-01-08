'''
Created on Dec 28, 2016

To understand the working of QFind refer to slides at 
https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
@author: pdesai
'''

class QUnion:
    QUImpdata=[]
    QUIblockdata=[]

    def __init__(self,xy_length=4):   
        self.QUImpdata=[]
        self.QUIblockdata=[]   
        for arrIndex in range(xy_length*xy_length):    
            self.QUImpdata.append(arrIndex)
            self.QUIblockdata.append(0)     
    
    def setBlockedSite(self,index):
        self.QUIblockdata[index] = 1

    def getBlockedSite(self,index):
        return self.QUIblockdata[index]
            
    def root(self,node):
        #print "root(",node,")"
        while(node != self.QUImpdata[node]):
            node= self.QUImpdata[node]
        return node
    
    def connected(self,node_a , node_b):
        #print "connected (",node_a,node_b,")"
        if(self.root(node_a) == self.root(node_b)):        
            return True
        else:
            return False        
   
    def union(self,node_a,node_b):
        #print "Union (",node_a,node_b,")"
        root_of_node_a = self.root(node_a)
        root_of_node_b = self.root(node_b)
        self.QUImpdata[root_of_node_a] = root_of_node_b
        #print self.QUImpdata
    
        
# x = QUnion(10)
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



