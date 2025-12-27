class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 +7
        n = len(corridor)

        s_count = corridor.count('S')
        if s_count ==0 or s_count %2 ==1:
            return 0
        
        total = 1
        sp = 0
        plants = 0
        for pos in corridor:
            if pos == "S":
                sp+=1

                if sp ==3:
                    sp = 1
                    total *= (plants + 1)
                    total %= mod
                    plants = 0
            else:
                # P
                if sp == 2:
                    plants+=1

        return total



            

