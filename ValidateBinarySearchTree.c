
bool isValidBST(struct TreeNode *root){
	struct TreeNode * p,* q;
	if (!root)
		return true;

	p = root->left;
	if(p)
	while(p->right)
		p = p->right;
	
	q = root->right;
	if(q)
	while(q->left)
		q = q->left;

	if ((p && p->val >= root->val) || (q && q->val <= root->val))
		return false;
	if (root->left)
		if(!isValidBST(root->left))
			return false;
	if (root->right)
		if(!isValidBST(root->right))
			return false;
	return true;
}
