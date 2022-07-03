import hashlib


class Merkle:
    
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
   

   def hash(self, val):
       return hashlib.sha256(val.encode('utf-8')).hexdigest()
   
   def doubleHash(self, hashed_val):
       return self.hash(hashed_val)
    

    
    
   def getRootHash(self):
       return self.rootHash
