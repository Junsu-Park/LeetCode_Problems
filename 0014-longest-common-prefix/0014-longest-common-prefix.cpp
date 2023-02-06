class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans = "";
        int max_length = 0;
            
        for (int i = 0; i < strs.size(); i++)
        {
            max_length = (max_length < strs[i].size()) ? strs[i].size() : max_length;
        }
        
        for (int i = 0; i < max_length; i++)
        {
            for (int j = 1; j < strs.size(); j++)
            {
                if(strs[j][i] != strs[j - 1][i])
                {
                    return ans;
                }
                
            }
            ans += strs[0][i];
        }
        
        return ans;
    }
};