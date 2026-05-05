class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        ma = 0
        for sell in prices[1:]:
            if sell > buy:
                ma = max(ma, sell - buy)
            else:
                buy = sell
        return ma
    
        
