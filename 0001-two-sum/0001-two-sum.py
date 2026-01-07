class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic={}
        for i,n in enumerate(nums):
            Diff = target - n 
            if Diff in dic:
                return [dic[Diff],i]
            dic[n]=i
        return []
