import hashlib

h = ["john","pinto","god"]


def hash(val):
    return hashlib.sha256(val.encode('utf-8')).hexdigest()
    
def doubleHash(val):
    return hash(val)


leaves = [doubleHash(e) for e in h]

for i in leaves:
    print(i)

        


