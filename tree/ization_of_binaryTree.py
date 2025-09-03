class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # slot checking method
        # binary tree property is:
            # every node consumes 1 slot
            # every non-null creates 2 new slot also
            # every null consumes 1 slot and doesn't creates any new
        
        preorder = preorder.split(',')
        slots = 1
        idx =0
        for i in range(len(preorder)):
            element = preorder[i]
            idx = i
            if element !="#":
                slots +=1
            else:
                slots -=1
            
            # print(element, slots)
            if slots <=0:
                break

        if slots == 0 and idx==(len(preorder)-1):
            return True
        return False
        
# optimal
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        for i in preorder.split(","):
            slots -=1
            if slots <0:
                return False

            if i !="#":
                slots+=2
                
        return slots ==0