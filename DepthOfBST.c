/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int max(int x,int y){
	if (x>y)
		return x;
	return y;
}

int maxDepth(struct TreeNode* root) {
    if (!root)
    	return 0;
    return max(maxDepth(root->left),maxDepth(root->right))+1;
}