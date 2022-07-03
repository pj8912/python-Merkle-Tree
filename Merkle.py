import hashlib


class Merkle:
    
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
