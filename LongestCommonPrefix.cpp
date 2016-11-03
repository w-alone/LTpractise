class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
                string s = "";
        if(strs.size() == 0)
            return s;
        if(strs.size() == 1)
            return strs[0];

        int end = 0;
        for(int i = 0;i < strs[0].size();i++)     // for going through each character of first string.
        {
            char c = strs[0][i];
            
            for(int j = 1;j < strs.size();j++)  // for going through ith character in each string
            {
                if(strs[j][i] == c)
                {
                    
                }
                else
                {
                    end = 1;
                    break;
                }
            }
            if(end == 1)
            {
                break;
            }
            s.push_back(strs[0][i]);
        }
        
        return s;

    }
};