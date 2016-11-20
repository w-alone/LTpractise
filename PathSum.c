bool hasPathSum_sub(struct TreeNode *root,int *sum)
{
	if (!root)
		return 0;
		
	*sum -= root->val;
	
	if (*sum==0 && root->left==NULL && root->right==NULL)
		return 1;

	if (root->left)
	{
		if(hasPathSum_sub(root->left,sum))
			return 1;
	}		
	
	if (root->right)
	{
		if(hasPathSum_sub(root->right,sum))
			return 1;
	}
	
    // if (*sum!=0 && root->left==NULL && root->right==NULL)
// 	{
	    *sum += root->val;
		return 0;
// 	}
	return 0;

}

bool hasPathSum(struct TreeNode *root,int sum)
{
	return hasPathSum_sub(root,&sum);
}
