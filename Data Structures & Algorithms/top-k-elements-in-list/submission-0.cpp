class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int x : nums) freq[x]++;

        int n = nums.size();
        vector<vector<int>> bucket(n + 1);

        for (auto &p : freq) {
            bucket[p.second].push_back(p.first);
        }

        vector<int> ans;
        for (int f = n; f >= 1 && (int)ans.size() < k; f--) {
            for (int x : bucket[f]) {
                ans.push_back(x);
                if ((int)ans.size() == k) break;
            }
        }

        return ans;
    }
};