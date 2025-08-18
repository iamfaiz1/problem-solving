class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.prevProd = [1]

    def add(self, num: int) -> None:
        val = self.prevProd[-1]
        if num==0:
            self.prevProd=[1]
        else:
            self.prevProd.append(num*val)
        self.arr.append(num)

    def getProduct(self, k: int) -> int:
        if len(self.prevProd) <= k:
            return 0
        return self.prevProd[-1]//self.prevProd[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)