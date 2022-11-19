class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        x= len(a)
        y= len(b)
        if x != y:
            return False
        d1={}
        for i in range(x):
            if a[i] in d1:
                d1[a[i]] += 1 
            else:
                d1[a[i]] = 1
        for i in range(x):
            if b[i] in d1:
                d1[b[i]] -= 1 
            else:
                return False
        for i in range(x):
            if d1[a[i]]<0:
                return False
        return True
