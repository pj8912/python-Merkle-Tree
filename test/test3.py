k = '001010001010101110101000101010101011110'

print(k[0])
#-------------------------------------

hex_nodes =[
        '001010001010101110101000101010101011110',
        'a4b785c6d774e9f97a38771b84bb40d127010870cef9ec6e76e7cdcc53931b6b',
        '5723360ef11043a879520412e9ad897e0ebcb99cc820ec363bfecc9d751a1a99' ]


node1 = hex_nodes[0]
print(node1)
print()


zero_count = 0
one_count = 0

for i in node1:
    if i == '0':
        zero_count +=1
 #   print('zeros:',zero_count)
    
    if i == '1':
        one_count += 1
#        print('ones:', one_count)

print('zeros:',zero_count)
print('ones:', one_count)
#--------------------------------------------------------
class Trees:

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def insert_node(self, node):
        if node[0] == '0':
            for bins in node:
                if bins == '0':
                    self.left.left = bins
                if bins == '1':
                    self.left.right = bins
        
        if node[0] == '1':
            for bins in node:
                if bins =='0':
                    self.right.left = bins
                else:
                    self.right.right  = bins 


tree = Trees(10, 0, 1)
tree.insert_node(node1)



