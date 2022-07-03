import hashlib


hex_nodes =[
        '96d9632f363564cc3032521409cf22a852f2032eec099ed5967c0d000cec607a', 
        'a4b785c6d774e9f97a38771b84bb40d127010870cef9ec6e76e7cdcc53931b6b', 
        '5723360ef11043a879520412e9ad897e0ebcb99cc820ec363bfecc9d751a1a99' ]


def convert2bin(val):
    scale = 16
    inbin = bin(int(val,scale))[2:].zfill(len(i)*4)
    return inbin




#create tree based on node's n-bit 0 or 1
#if n^th bit is '0' - left
#if 1 - right

class KademliaTree:

    def __init__(self,value):
        self.value = value
        self.left = 0
        self.right = 1


    def insert_node(self, node):
        nth_bit = node[0]
        if node[0] == 0:
            pass 
        else node[0] == 1:
            pass
    



if __name__ == '__main__':
    
    for i in hex_nodes:
        bin_val = convert2bin(i)
        




