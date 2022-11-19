class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        x= len(s)
        y= len(goal)
        if x != y:
            return False
        for i in range(x):
            if s[i:]+s[:i] == goal:
                return True
        return False
