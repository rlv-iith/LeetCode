class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp =0
        tp =0
        if len(s)==0:
            return True
        while tp<len(t):
            if s[sp]==t[tp]:
                sp+=1
            if sp==len(s):
                return True
            tp+=1
        return False 