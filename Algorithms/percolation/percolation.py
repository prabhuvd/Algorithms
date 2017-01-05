'''
Created on Dec 29, 2016
This is the main file 
@author: pdesai
'''
import random
import pygame
import logging
from numpy import average
import time
import QUnionImprove
import VisualizeData
 
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.propagate = False

UPDATE_500MS_TIMER = 0.5
XY_MATRIX_LENGTH = 10
BLOCK_WIDTH=40

XY_MATRIX_INCLUDING_VNODES = XY_MATRIX_LENGTH +1
TOTAL_NODES  = XY_MATRIX_LENGTH  * XY_MATRIX_LENGTH 
ENTIRE_RANGE = range(1,TOTAL_NODES+1)
SCREEN_WIDTH = BLOCK_WIDTH*XY_MATRIX_LENGTH+200
SCREEN_HEIGHT= BLOCK_WIDTH*XY_MATRIX_LENGTH+200

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (100, 255, 100)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (165,42,42)
MAROON = (128, 0, 0)

global_opened_sites=[]
global_start_time=0 
global_check_timer = False
global_simulate_once = False
global_screen=0
 
instance_viz_data = VisualizeData.VisualizeData(XY_MATRIX_LENGTH,BLOCK_WIDTH)
  
pygame.init()
 
# Set the width and height of the  screen [width, height]
global_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
pygame.display.set_caption("Percolation Simulation")
global_bigFont = pygame.font.SysFont("None",25)
global_mediumFont = pygame.font.SysFont("None",20)
global_smallFont = pygame.font.SysFont("None",15)

# render text
txtSimInstruction = global_bigFont.render("Simulation , Continuous: press 5 , Single : press 0 ", 1, BLUE)
global_screen.blit(txtSimInstruction, (0, 0)) 

txtsimResulttxt=global_bigFont.render("Average Probability = "+"0", 1, BROWN)
txtPercNodes=global_mediumFont.render("Opened Nodes="+"0", 1, BLUE)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the global_screen updates
clock = pygame.time.Clock()
 
'''
Returns a random block as open , the random generation is repeated 
if the block is already open 
open  
''' 
def getRandomSite(omap):
    global global_opened_sites

    opensite = random.choice(ENTIRE_RANGE)
        
    while opensite in global_opened_sites:
        opensite = random.choice(ENTIRE_RANGE)
    
    global_opened_sites.append(opensite) 
    omap.setBlockedSite(opensite)
    return opensite

'''
- Create the virtual nodes  at the top and the bottom
- Set the vizualtion data array to 0 (indicating blocked)
''' 
def initNodes():         
    global global_opened_sites
    x = QUnionImprove.QUnionImprove(XY_MATRIX_INCLUDING_VNODES)

    #Create upper virtual node : 0 
    upperVirtualNode = 0 
    for toprownodes in range(1,XY_MATRIX_INCLUDING_VNODES):
        x.union(toprownodes,upperVirtualNode)
    #Create bottom virtual node : TOTATL_NODES +1
    bottomVirtualNode = TOTAL_NODES+1
    
    for bottomnodes in range(TOTAL_NODES+1-XY_MATRIX_LENGTH,TOTAL_NODES+1):
        x.union(bottomnodes,bottomVirtualNode)
    global_opened_sites=[] 
    instance_viz_data.clearAllBlocks()
    logger.debug(x.getQUImpData())
    return x

'''
Create union between two cells on the given map
''' 
def createUnion(val,osite,nodes):    
    if(val>0) and (val<=XY_MATRIX_LENGTH*XY_MATRIX_LENGTH) and nodes.getBlockedSite(val)>0  :
        nodes.union(val,osite)

'''
Check adjacent around osite in the input matrxix array (omap) 
'''     
def checkAdjacentBlocks(osite,nodes):
    # Check the four corners
    left  = osite - 1
    right = osite + 1
    up    = osite - XY_MATRIX_LENGTH
    down  = osite + XY_MATRIX_LENGTH    
    logger.debug (" - Left , right , up , down -> %s ,%s ,%s,%s",left,right, up, down)
    
    # There is no left for cells on the first column
    if((osite+XY_MATRIX_LENGTH-1) % XY_MATRIX_LENGTH) != 0:        
        createUnion(left,osite,nodes)
    # There is no RIGHT for cells on the last column
    if(osite % XY_MATRIX_LENGTH ) != 0:
        createUnion(right,osite,nodes)
    
    createUnion(up,osite,nodes)
    createUnion(down,osite,nodes)

'''
Update global_screen with open & closed blocks
Update text information
'''
def updateScreen():
    global global_screen
    index=0
    # Display instruction for simulation
    global_screen.blit(txtSimInstruction, (0, 0))
    # Display average probability number 
    global_screen.blit(txtsimResulttxt, (SCREEN_WIDTH-300, 0))
    # Display all the open nodes created during simulation
    global_screen.blit(txtPercNodes, (0, 20))
    
    for xyblock in instance_viz_data.getdataCoOrdinates():
        if(instance_viz_data.getdataBlock(index) == True):
            pygame.draw.rect(global_screen,GREEN,xyblock,0)
        else:           
            pygame.draw.rect(global_screen,BLACK,xyblock,1)
            
        txtNodeNum=global_smallFont.render(str(index+1), 1, BROWN)
        global_screen.blit(txtNodeNum, (xyblock[0], xyblock[1]))  
        index= index+1
        
'''
Waiting for keyboard input to start single or multiple simluations. 
''' 

local_done=False

while not local_done:
    local_percolated_list=[]
    local_nodes=[]
    local_val=0
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            local_done = True
        elif event.type == pygame.KEYDOWN:
            #Simulation in continuous mode every 500ms    
            if event.key == pygame.K_5: 
                global_check_timer=True
                global_simulate_once=False        
                global_start_time = time.time()
            #Simulate once and stop !! 
            elif event.key == pygame.K_0: 
                global_simulate_once=True  
                global_check_timer= False             
                    
    if ((global_check_timer == True) and ((time.time() - global_start_time) >= UPDATE_500MS_TIMER)) \
        or (True==global_simulate_once):      
        global_start_time = time.time()
        global_simulate_once= False
                
        local_nodes = initNodes()
        for i in range(TOTAL_NODES):
            local_val = getRandomSite(local_nodes)
            logger.debug(global_opened_sites)
            #logger.debug("Random Cell %d",val)
            instance_viz_data.setdataBlock(local_val-1)                  
            checkAdjacentBlocks(local_val,local_nodes)
                   
            if( True == local_nodes.connected(0, TOTAL_NODES+1)):
                logger.debug("Percolated at block =%d", i+1)
                logger.debug(global_opened_sites) 
                local_percolated_list.append((i+1)/float(TOTAL_NODES))
                txtsimResulttxt = global_bigFont.render("Probability = "+str(average(local_percolated_list)), 1, BROWN)
                txtPercNodes = global_mediumFont.render("Opened Nodes="+str(global_opened_sites), 1, MAROON)                        
                break          
        
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the global_screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    global_screen.fill(WHITE)    
     
    # --- Drawing code should go here
    updateScreen()

    # --- Go ahead and update the global_screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(100)
 
# Close the window and quit.
pygame.quit()


