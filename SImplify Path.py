class Solution:
    def simplifyPath(self, path: str) -> str:
        new_paths = []
        paths = path.split('/')
        for p in paths:
            if p == '..':
                if len(new_paths) > 0:
                    new_paths.pop()
            elif p != '' and p != '.':
                new_paths.append(p)
        
        final = '/'
        for i in new_paths:
            final += i + '/'
        if len(final) > 1:
            final = final[:-1]
        return final
