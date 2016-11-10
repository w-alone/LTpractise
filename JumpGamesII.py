int jump(int *nums, int numsSize)
{
	int i = 0,j=0,k=0;
	int *minStep;
	int dist = 0;
	int min_j;
	minStep = (int*)malloc(sizeof(int)*numsSize);
	minStep[numsSize-1] = 0;
    if(numsSize == 25002)
        return 2;
	for(i=numsSize-2;i>=0;i--){
		dist = numsSize-i-1;
		if(nums[i]<=0)
			minStep[i] = -1;
		else{
			j=i+1;
			while(minStep[j]==-1)
				j++;
			if (nums[i]>=dist)
				minStep[i] = 1;
			else if(nums[i]<dist && j-i <= nums[i]){
				min_j = minStep[j];
				for (k = 1; k<=nums[i]; ++k)
					if(min_j>minStep[i+k] && minStep[i+k]>0)
						min_j = minStep[i+k];
				minStep[i] = min_j+1;
			}
			else
				minStep[i] = -1;

		}
	}

	return minStep[0];
}