from copy import deepcopy


class Solution:
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []
        else:
            num2letter = {
                '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
            }
            if len(digits) == 1:
                return [i for i in num2letter.get(digits)]
            letters = [num2letter.get(i) for i in digits]
            vals = []
            temp_vals = deepcopy([i for i in letters[0]])
            temp = []
            for i in range(1, len(letters)):
                for j in letters[i]:
                    temp = self.add_vals(deepcopy(temp_vals), j)
                    for k in temp:
                        vals.append(k)
                temp_vals = deepcopy(vals)
            return_val = [i for i in vals if len(i) == len(digits)]
            return sorted(return_val)

    def add_vals(self, new_vals, char):
        for i in range(len(new_vals)):
            new_vals[i] += char
        return new_vals