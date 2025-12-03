class Solution:
    def maxProfit(self, prices: list):
        best = 0
        current_pos=0
        buy_pos=0
        for price in prices:
            if prices[current_pos] < prices[buy_pos]:
                buy_pos = current_pos
            if prices[current_pos] > prices[buy_pos]:
                if prices[current_pos] - prices[buy_pos] > best:
                    best = prices[current_pos] - prices[buy_pos]
            current_pos+=1
        return best

solution= Solution()
print(solution.maxProfit([7,1,5,3,6,4])) # 5
print(solution.maxProfit([7,6,4,3,1])) # 0