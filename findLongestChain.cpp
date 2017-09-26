class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        sort(pairs.begin(),pairs.end(),[](vector<int> a,vector<int> b){
        	return a[0]<b[0];
        });
        const int n = pairs.size();
        std::vector<int> v(n,1);
        for (int i = 1; i < n; ++i)
        	for (int j = 0; j < i; ++j)
        		if(pairs[i][0] > pairs[j][1])
        			dp[i] = max(dp[i],dp[j]+1);
        return max_element(dp.begin(), dp.end());
    }
};