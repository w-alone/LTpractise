class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        if(obstacleGrid[m-1][n-1])
        	return 0;
        int i ,j;
        cout << m << "  " << n << endl;
        vector<vector<int> > dp(m,vector<int>(n,0));
        for(j=n-1;j>=0;j--)
        	if(!obstacleGrid[m-1][j])
        		if(j<n-1 && dp[m-1][j+1])
        			dp[m-1][j] = 1;
        		else if(j==n-1)
        			dp[m-1][j] = 1;
        for(i=m-1;i>=0;i--)
        	if(!obstacleGrid[i][n-1])
        		if(i<m-1 && dp[i+1][n-1])
	        		dp[i][n-1] = 1;
	        	else if(i==m-1)
	        		dp[i][n-1] = 1;
		for (i = m-2; i >= 0; --i)
			for(j = n-2; j>=0; --j)
				if(!obstacleGrid[i][j])
					dp[i][j] = dp[i+1][j]+dp[i][j+1];
        return dp[0][0];
    }
};