class Solution:
    v = 0
    def addBinary(self, a: str, b: str) -> str:
        c = f'new_a, new_b = 0b{a}, 0b{b} \nprint(new_a, new_b) \nglobal v \nv = bin(new_a + new_b)'
        exec(c)
        return v[2:]
        