'''
Created on Dec 30, 2016

@author: pdesai
'''
'''   
 The hieght and widht of the block is the same 
 and is defined by __blockWidth
     ------
    |     |     
    ------
'''
class VisualizeData:
    SCREE_OFFSET=50
    def __init__(self,row_columns=4,blockWidth=80):
        self.__rowCol = row_columns
        self.__blockWidth = blockWidth       
        self.__vizNodes = [0]*(self.__rowCol*self.__rowCol)
        self.__nodeCoOrdinates=[]
        #print self.__vizNodes            
        self.generateBlocks()
    
    def generateBlocks(self):     
        for row in range(self.__rowCol):
            for x in range(self.__blockWidth,self.__blockWidth+self.__blockWidth*self.__rowCol,self.__blockWidth):
                self.__nodeCoOrdinates.append([self.SCREE_OFFSET+x,self.SCREE_OFFSET+self.__blockWidth*(row+1),self.__blockWidth,self.__blockWidth]) 
    
    def setdataBlock(self,index):        
        self.__vizNodes[index] = True    

    def cleardataBlock(self,index):        
        self.__vizNodes[index] = False 
    
    def getdataBlock(self,index):        
        return self.__vizNodes[index]
    
    def getdataCoOrdinates(self):        
        return self.__nodeCoOrdinates 
       
    def clearAllBlocks(self):
        self.__vizNodes = [0]*(self.__rowCol*self.__rowCol)