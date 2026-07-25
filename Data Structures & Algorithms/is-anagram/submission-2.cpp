class Solution {
public:
    bool isAnagram(string s, string t) {
        int chars[26] = {0};
        if (s.length() != t.length()) return false;

        for (int i = 0; i<s.length(); i++) {
            chars[s[i] - 'a']++;
            chars[t[i] - 'a']--;
        }

        for (int c: chars) {
            if (c != 0) return false;
        }
        return true;
    }
};
