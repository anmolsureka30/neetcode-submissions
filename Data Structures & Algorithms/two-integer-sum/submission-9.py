class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            req = target - nums[i]
            d={val:idx for idx,val in enumerate(nums)}
            if req in d:
                if d[req] != i:
                    return [i, d[req]]
                        
            




