class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
    	const int size = nums.size();
        if(size == 0)
            return 0;
    	std::vector<int> dp(size,1);
    	std::vector<int> dpt(size,0);
    	dpt[0] = 1;
    	std::vector<int> num(size+1,0);
    	for (int i = 1; i < size; ++i){
    		dpt[i] = 1;
    		for (int j = 0; j < i; ++j){
    			if(nums[i]>nums[j]){
					if(dp[i] < dp[j]+1){
						dp[i] = dp[j]+1;
						dpt[i] = dpt[j];
					}
					else if(dp[i] == dp[j]+1)
						dpt[i] += dpt[j];
    			}
    		}
    		num[dp[i]] += dpt[i];
    	}
    	for (int i = size; i > 1; --i)
    		if(num[i] != 0)
    			return num[i];
        // cout <<"d"  << endl;
    	return size;
    }
};