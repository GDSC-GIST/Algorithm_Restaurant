# 56ms, 13.9MB, -27..
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        r, c = (len(s), len(p))
        if r == 0 and c == 0:
            return True
        if c == 0:
            return False
        
        # dp[i][j] -> s[:i]가 p[:j]로 표현되는지
        dp = [[False for j in range(c + 1)] for i in range(r + 1)]
        dp[0][0] = True
        
        # 첫 줄 초기화
        for i in range(2, c + 1):
            # i가 0일 때 반드시 j도 0이어야 함
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                # 지금이 같으면 이전꺼만 같으면 전부 되는거임
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif j > 1 and p[j - 1] == '*':
                    # 반복일 때 0개
                    dp[i][j] = dp[i][j - 2]
                    # 반복일 때 1개 이상
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[r][c]