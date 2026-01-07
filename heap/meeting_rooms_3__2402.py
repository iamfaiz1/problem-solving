class Solution:
    def mostBooked(self, n: int, meet: List[List[int]]) -> int:
        import heapq
        # sort
        meet.sort(key = lambda x: x[0])
        
        record = [[0, 0] for _ in range(n)]  # [end_time, count]
        free = list(range(n))   #free room indexs
        busy = []
        
        heapq.heapify(free)

        for s, e in meet:
            # new room search krne se phle jo used rooms hai agr woh free hogye hai toh unko hi fill krloo.. kya zrurat new room occupy krne ki

            # actually room free kr rhe uski sfai krre!
            while busy and busy[0][0] <= s:
                _, k = heapq.heappop(busy)
                heapq.heappush(free, k)
    
             # if room available
            if free:
                k = heapq.heappop(free)
            else:
                # delay meeting
                mi, k = heapq.heappop(busy)
                d = e-s
                s = mi
                e = s + d
            
            # assign delayed meeting
            record[k][0] = e
            record[k][1] +=1
            heapq.heappush(busy, (e, k))

        j = 0
        for i in range(n):
            if record[j][1] < record[i][1]:
                j = i
        return j


# ----------------------------------------------------------------------------------
# --                     bruteforece: doule loop (passed)                         --
# ----------------------------------------------------------------------------------

class Solution:
    def mostBooked(self, n: int, meet: List[List[int]]) -> int:
        # sort
        meet.sort(key = lambda x: x[0])
        ln = [[0, 0] for _ in range(n)]  # [end_time, count]

        for s, e in meet:
            k = -1

            # if room found
            for i in range(n):
                if ln[i][0] <= s:
                    k = i
                    break
            
            # if no room is free, fin min delay
            if k == -1:
                mi = float('inf')
                for i in range(n):  #finding min end time
                    if mi > ln[i][0]:
                        mi = ln[i][0]
                        k = i
                d = e-s
                s = mi
                e = s + d

            # assign delayed meeting
            ln[k][0] = e
            ln[k][1] +=1

        j = 0
        for i in range(n):
            if ln[j][1] < ln[i][1]:
                j = i
        return j
