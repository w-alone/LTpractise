int removeDuplicates(int* nums, int numsSize) {
   int start=0; // where we put new value
   int i = 0; 
   int dup_num=0;

   if (numsSize<=2)
   		return numsSize;

   for (i = 0; i < numsSize-2; ++i){
   		if (nums[i]!=nums[i+2])
   		{
   			nums[start] = nums[i];
   			start++;
   		}
   }
   nums[start++] = nums[numsSize-2];
   nums[start++] = nums[numsSize-1];

   return start;
}
