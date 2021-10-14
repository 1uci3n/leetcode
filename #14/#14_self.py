class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num_strs = len(strs)
        min_len = len(strs[0])
        if num_strs == 1:
            return strs[0]
        for i in range(1, num_strs):
            if min_len > len(strs[i]):
                min_len = len(strs[i])
        prefix = ""
        for i in range(min_len):
            current_str = strs[0][i]
            for j in range(1, num_strs):
                if current_str != strs[j][i]:
                    return prefix
            prefix += current_str
        return prefix
