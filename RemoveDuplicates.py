int removeDuplicates(int* nums, int numsSize) {
   int start=0; // where we put new value
   int travse;
   int i = 0; 
   if(numsSize==0)
    return 0;
   for (i = 0; i < numsSize-1; ++i){
   		if (nums[i]!=nums[i+1])
   		{
   			nums[start] = nums[i];
   			start++;
   		}
   }
   if (nums[numsSize-1]!=nums[start-1])
   		nums[start] = nums[numsSize-1];

   	return start +1;
}