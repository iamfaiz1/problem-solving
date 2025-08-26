class Solution:
    def aggressiveCows(self, stalls, k):
        # code here
        stalls.sort()
        res = 0
        left = 1
        right = stalls[-1]-stalls[0]
        
        while(left<= right):
            mid = left + (right-left)//2
            cow = stalls[0]
            done = 1
            
            for i in range(1, len(stalls)):
                if stalls[i]-cow >= mid:
                    cow = stalls[i]
                    done +=1
                
            if done >= k:
                res = max(res, mid)
                left = mid +1
            elif done <k:
                right = mid -1
                
        return res
        
        