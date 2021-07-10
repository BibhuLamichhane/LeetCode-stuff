class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        o = []
        x = [sorted(i) for i in strs]
        for i in range(len(strs)):
            val = []
            if x[i] is not None:
                temp = x[i]
                val.append(strs[i])
                x[i] = None
                while temp in x:
                    curr = x.index(temp)
                    val.append(strs[curr])
                    x[curr] = None
                o.append(val)
        return o