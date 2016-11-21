int maxProfit(int* prices, int pricesSize) {
	int i=0 , j=1 ,profit=0;
	int temPro;
	while(j<pricesSize){
		temPro = prices[j] - prices[i];
		if(temPro > profit)
			profit = temPro;
		if (prices[j]<prices[i])
			i=j;
		j++;
	}
	return profit;
}