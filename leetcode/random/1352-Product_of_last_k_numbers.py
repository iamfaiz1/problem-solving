class ProductOfNumbers:
# 1352. Product of the Last K Numbers
# look we dont actually need to store all numbers, just the product

    def __init__(self):
        # self.arr = []
        self.prevProd = [1]

    def add(self, num: int) -> None:
        val = self.prevProd[-1]
        if num==0:
            self.prevProd=[1]
        else:
            self.prevProd.append(num*val)
        # self.arr.append(num)

    def getProduct(self, k: int) -> int:
        # this is to handle 0 input case
        # we adjusted the prefix product array to [1] in case of zero
        if len(self.prevProd) <= k:
            return 0
        
        return self.prevProd[-1]//self.prevProd[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)