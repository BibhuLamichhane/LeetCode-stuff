class Solution:

    def convert(self, s: str, numRows: int) -> str:
        rows = []
        now = True
        counter = 0
        output = ''
        if numRows > len(s):
            numRows = len(s)
        if len(s) <= 1 or numRows == 1:
            return s
        for i in range(numRows):
            rows.append([s[counter]])
            counter += 1
        while counter < len(s):
            for i in range(numRows - 2, -1, -1):
                if counter < len(s):
                    rows[i].append(s[counter])
                    counter += 1
            for i in range(1, numRows):
                if counter < len(s):
                    rows[i].append(s[counter])
                    counter += 1
        for row in rows:
            for r in row:
                output += r
        return output