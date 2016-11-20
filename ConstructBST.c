/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* iterbuild(struct TreeNode *root, int* inorder, int* postorder, int li, int ri, int lp, int rp){
    if (li<0 || ri<li || lp<0 || rp<lp)
		return NULL;
	int counter=li;
	int leftNum,rigNum;
	int size = ri-li+1;
	while(inorder[counter]!=postorder[rp])
		counter++;
	leftNum = counter-li;
	rigNum = size-leftNum-1;
	root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
	root->val = postorder[rp];
	//printf("val is %d, li:%d , ri:%d , lp:%d rp:%d\n", root->val,li,ri,lp,rp);
	if(leftNum<=0)
		root->left = NULL;
	else
		root->left = iterbuild(root->left,inorder,postorder,li,counter-1,lp,lp+leftNum-1);
	
	if(rigNum<=0)
		root->right = NULL;
	else
		root->right = iterbuild(root->right,inorder,postorder,counter+1,ri,lp+leftNum,rp-1);
	return root;
} 


struct TreeNode* buildTree(int* inorder, int inorderSize, int* postorder, int postorderSize) {
    if(inorderSize==0)
    	return NULL;
    struct TreeNode  *root;
    return iterbuild(root,inorder,postorder,0,inorderSize-1,0,inorderSize-1);
}