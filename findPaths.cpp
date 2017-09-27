class Solution {
public:
    int findPaths(int m, int n, int N, int i, int j) {
        long int dp[51][50][50] = {};
    	for (int mi = 1; mi <= N; ++mi)
    		for (int mj = 0; mj < m; ++mj)
    			for (int k = 0; k < n; ++k)
    				dp[mi][mj][k] = ((mj==0?1:dp[mi-1][mj-1][k])+(mj==m-1?1:dp[mi-1][mj+1][k])+(k==0?1:dp[mi-1][mj][k-1])+(k==n-1?1:dp[mi-1][mj][k+1]))%1000000007;
    	return dp[N][i][j];
    }
};

