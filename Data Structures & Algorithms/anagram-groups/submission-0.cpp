class Solution {
public:
    int anagramInVec(string str, vector<vector<string>> a) {
        for (int i = 0; i<a.size(); i++) {
            if (is_permutation(a[i][0].begin(), a[i][0].end(), str.begin()) && a[i][0].length() == str.length()) {
                return i;
            }
        }
        return -1;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;

        for (string s: strs) {
            int b = anagramInVec(s, res);
            if (b == -1) {
                res.push_back({s});
            } else {
                res[b].push_back(s);
            }
        }
        return res;
    }
};
