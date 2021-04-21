class Solution:
    class Node:
        def __init__(self):
            self.children = {}

    def wordBreak(self, s, wordDict):
        ok = [False] * (len(s) + 1)
        ok[0] = True
        for i in range(1, len(s) + 1):
            ok[i] = any([ok[j] and s[j:i] in wordDict for j in range(i)])
        return ok[-1]