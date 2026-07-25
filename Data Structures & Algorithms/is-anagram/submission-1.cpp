class Solution {
public:
    bool isAnagram(string s, string t) {
        return is_permutation(s.begin(), s.end(), t.begin()) && s.length() == t.length();
    }
};
