class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> mp;

        for (int i = 0; i<strs.size(); i++) {
            int freq[26] = {0};
            for (char c: strs[i]) {
                freq[c-'a']++;
            }

            string key = "";
            for (int i = 0; i < 26; i++) {
                key += to_string(freq[i]) + "_";
            }

            if (mp.find(key) == mp.end()) {
                mp[key] = {strs[i]};
            } else {
                mp[key].push_back(strs[i]);
            }
        }

        vector<vector<string>> res;
        for (auto it: mp) {
            res.push_back(it.second);
        }
        return res;
    }
};
