def maxProfit(prices):
        buy = float('inf') 
        sell = 0
        for i in range(len(prices)):
            
            if prices[i] < buy:
                buy= prices[i]
                
            profit = prices[i] - buy


            if profit > sell:
                sell = profit

        return sell
print(maxProfit([7,1,5,3,6,4]))