/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  struct TreeLinkNode *left, *right, *next;
 * };
 *
 */
void connect(struct TreeLinkNode *root) {
    if(!root || !root->left)
    	return ;
    struct TreeLinkNode *p1,*p2;
    root->left->next = root->right;
    connect(root->left);
    connect(root->right);
    p1 = root->left->right;
    p2 = root->right->left;
    while(p1){
    	p1->next = p2;
    	p1 = p1->right;
    	p2 = p2->left;
    }
}