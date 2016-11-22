class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        if(size<=1)
            return 0;
        int profit = 0;
        int buy = prices[0];
        for (int i = 1; i < size; ++i){
            if(buy>=prices[i])
                buy = prices[i];
            else{
                if((i<size-1 && prices[i]>prices[i+1])||(i==size-1))
                    profit += (prices[i]-buy);
                if(i<size-1 && prices[i]>prices[i+1])
                    buy = prices[i+1];
            }
        }
        return profit;
    }
};