/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    bool carry = 1;
    int i = digitsSize-1;
    for (; i>=0 && carry ; --i)
    {
		if (digits[i]==9)
			digits[i] = 0;
		else{
			digits[i] += 1;
			carry = 0;
		}
	}
	if (carry)
	{
		*returnSize = digitsSize+1;
		int *result = (int*)malloc(sizeof(int)*(*returnSize));
		result[0] = 1;
		for(i=0;i<digitsSize;i++)
			result[i+1] = digits[i];
		return result;
	}
	*returnSize = digitsSize;
	return digits;
}