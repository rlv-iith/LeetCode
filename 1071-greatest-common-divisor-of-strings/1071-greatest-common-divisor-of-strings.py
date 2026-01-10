class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1,len2=len(str1),len(str2)
        for i in range(min(len1,len2),0,-1):
            if len1%i!=0 or len2%i!=0:
                continue
            candidate=str1[:i]
            multiple1=len1//i
            multiple2=len2//i
            if (candidate*multiple1==str1) and (candidate*multiple2==str2):
                return candidate
            return ""