'''
Created on Nov 29, 2016

@author: pdesai
'''
import id_list
import binascii

def get_clean_hex(inhex):
    # Remove "0x" at the beginning and "L" at the end
    return (hex(inhex)[2:])[:8]

def byte_to_binary(n):
    return ''.join(str((n & (1 << i)) and 1) for i in reversed(range(8)))

def hex_to_binary(h):
    return ''.join(byte_to_binary(ord(b)) for b in binascii.unhexlify(h))

def merge_list(inlist,start,end):
    return ''.join(inlist[start:end])

def get_8_bits(inlist,start):    
    return hex(int(''.join(inlist[start:start+8]), 2))
 
    
def scan_Data(wuppattern):    
    binlist=  list(hex_to_binary(wuppattern))    
    for scan_start in range(len(binlist)-8):
        tmp= get_8_bits(binlist,scan_start)
        if("0x89" == tmp):
            print "WUP:",wuppattern,"0x89 matched @bit_position",scan_start,merge_list(binlist,0,scan_start),"->",merge_list(binlist,scan_start,31)
 
 
for id_s in id_list.ALL_POSSIBLE_ID:     
    scan_Data(id_s)
 

