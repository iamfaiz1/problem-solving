class Solution:
    def countCollisions(self, directions: str) -> int:
        di = list(directions)
        count = 0
        start = 0
        end = len(di)

        # left-movers trimming
        for i in di:
            if i=='L':
                start +=1
                continue
            break
        # right-movers trimming
        for i in range(len(di)-1, -1, -1):
            if di[i]=='R':
                end -=1
                continue
            break
        
        for i in range(start, end):
            if di[i]!='S':
                count+=1
        return count
        
             
            

        