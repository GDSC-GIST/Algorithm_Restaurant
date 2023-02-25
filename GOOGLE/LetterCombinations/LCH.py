from itertools import product

# 32ms, 13.9MB, 0
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        db = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        chars = []
        for i in map(int, list(digits)):
            chars.append(db[i])
        if digits:
            return ["".join(x) for x in product(*chars)]
        return []
