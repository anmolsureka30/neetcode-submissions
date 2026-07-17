class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist=list(s)
        tlist=list(t)
        a=[]
        b=[]
        for x in slist:
            a.append(ord(x)-ord('a'))
        a.sort()   
        for y in tlist:
            b.append(ord(y)-ord('a'))
        b.sort() 
        return a==b       


