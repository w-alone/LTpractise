void sortColors(int* nums, int numsSize) {
    int redSize=0 , whiteSize=0 , blueSize=0;
    int i;
    for (i = 0; i < numsSize; ++i)
    {
    	if(nums[i]==0)
    		redSize += 1;
    	else if(nums[i]==1)
    		whiteSize += 1;
    	else
    		blueSize += 1;
    }
    for(i=0; i < redSize; i++)
    	nums[i]=0;
    for(i=redSize; i < redSize+whiteSize; i++)
    	nums[i]=1;
    for (i = redSize+whiteSize; i < redSize+whiteSize+blueSize; ++i)
    	nums[i]=2;
}