/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
		vector<vector<int>> result;
		
		if (!root)
			return result;

		stack<TreeNode*> Stack1;
		stack<TreeNode*> Stack2;
		int level = 0;
		TreeNode *p = root;
		Stack1.push(p);
		bool rtag = 1;
		std::vector<int> v;
		while(!Stack1.empty() || !Stack2.empty()){			
			while(!Stack1.empty()){
				p = Stack1.top();
				Stack1.pop();
				if(p->left)
					Stack2.push(p->left);
				if(p->right)
					Stack2.push(p->right);
				v.push_back(p->val);				
			}
			if(!v.empty()){
				result.push_back(v);
				v.clear();
			}
			
			while(!Stack2.empty()){
				p = Stack2.top();
				Stack2.pop();
				if (p->right)
					Stack1.push(p->right);
				if (p->left)
					Stack1.push(p->left);
				v.push_back(p->val);
			}
			if(!v.empty()){
				result.push_back(v);
				v.clear();
			}
		}
        return result;
    }//vector<vector<int>>
   
};
