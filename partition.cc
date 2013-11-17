class Solution {
public:
    vector<vector<string>> partition(string s) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        vector<vector<string>> ret;
        if (!s.size()) return ret;
        return _partition(s, 0, s.size() - 1);
    }
    
    vector<vector<string>> _partition(string &s, int start, int end) {
        vector<vector<string>> ret;
        if (start > end) {
            ret.push_back(vector<string> ());
            return ret;
        }
        for (int i = start; i <= end; i++) {
            if (check(s, start, i)) {
                vector<vector<string>> tmp = _partition(s, i + 1, end);
                for (int j = 0; j < tmp.size(); j++) {
                    tmp[j].insert(tmp[j].begin(), s.substr(start, i - start + 1));
                }
                ret.insert(ret.end(), tmp.begin(), tmp.end());
            }
        }
        return ret;
    }
    
    bool check(string &s, int start, int end) {
        while (start <= end) {
            if (s[start] != s[end])
                return false;
            start++;
            end--;
        }
        return true;
    }
};