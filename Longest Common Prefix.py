class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        prefixes = [""]
        flag = True
        if len(strs) > 0:
            while i <= len(strs[0]):
                prefix = strs[0][:i]
                for j in strs:
                    try:
                        if j[:i] != prefix:
                            flag = False
                    except:
                        pass
                i += 1
                if flag:
                    prefixes.append(prefix)
        lengths = [len(p) for p in prefixes]
        index = lengths.index(max(lengths))
        return prefixes[index]
            