class Solution:
    # ye hai aam zindagiiii
    def integerBreak(self, n: int) -> int:
        m = 0
        # recursion
        def fun(num):

            if num==2:
                return 1
            elif num==3:
                return 2
            
            m=0
            for i in range(1, num):
                m = max(m, i*(num-i), i*fun(num-i))
            return m
        return fun(n)
# _______________________________________________________

# ye hai mentos zindagi (optimised order-n)
class Solution:
    def integerBreak(self, n: int) -> int:
        # max product is given when two small noo multiply then one big and one very small::
        # ideal is 3*3*3 but if remiander is 1 then consider
        # 3*3*3*3...*4

        if n == 2:
            return 1
        elif n == 3:
            return 2

        product = 1
        q, r = divmod(n, 3)
        while n > 4:
            product *= 3
            n -= 3
            # agr n=4, toh multiply
            # agr n=3, toh koi dikkt ni multiply ho jyga
            # agr n=2, toh multiply krna hi pdegaa
        return product * n


#___________________________________________________________
# most optimiseddddd order-1
class Solution:
    def integerBreak(self, n: int) -> int:
        # max product is given when two small noo multiply then one big and one very small::
        # ideal is 3*3*3 but if remiander is 1 then consider
        # 3*3*3*3...*4

        if n == 2:
            return 1
        elif n == 3:
            return 2

        q, r = divmod(n, 3)
        if r==1:
            product = 3**(q-1)*4
        elif r==2:
            product = 3**(q)*2
        else:
            product = 3**q
        return product
        
