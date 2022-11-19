class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        AB,BA={},{}
        if len(str1)!=len(str2):
            return False
        for i in range(len(str1)):
            c1= str1[i]
            c2= str2[i]
            if (c1 in AB and AB[c1]!=c2) or (c2 in BA and BA[c2]!=c1):
                return False
            AB[c1]= c2
            BA[c2]= c1
        return True
