class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        prefixes = [""]
        flag = True
        while i <= len(strs[0]):
            prefix = strs[0][:i]
            for j in strs:
                if prefix not in j:
                    flag = False
            i += 1
            if flag:
                prefixes.append(prefix)
            lengths = [len(p) for p in prefixes]
            index = lenghts.index(max(lengths))
            return prefixes[index]
            