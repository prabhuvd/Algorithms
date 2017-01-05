'''
Created on Dec 28, 2016

@author: pdesai
'''
class QFind:
    QUImpdata=[]
    #Constructor ...
    def __init__(self,length=10):        
        for arrIndex in range(length):    
            self.QUImpdata.append(arrIndex)     
     
    def connected(self,node_a , node_b):
        print "connected (",node_a,node_b,")"
        if(self.QUImpdata[node_a] == self.QUImpdata[node_b]):        
            return True
        else:
            return False        
    
    def union(self,node_a,node_b):
        print "Union (",node_a,node_b,")"
        for index in range(len(self.QUImpdata)):
            if(self.QUImpdata[index] == node_a ):
                self.QUImpdata[index] = self.QUImpdata[node_b]
        print self.QUImpdata        
        return False
    
x = QFind(10)

x.union(4,3)

print x.connected(3, 4)
print x.root(3)
print x.root(4)

x.union(3,8)
x.union(6,5)
x.union(9,4)
x.union(2,1)
 
x.union(5,0)
x.union(7,2)
x.union(6,1)
x.union(7,3)    


