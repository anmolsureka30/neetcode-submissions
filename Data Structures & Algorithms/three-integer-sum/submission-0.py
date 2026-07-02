class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_list = []
        hashmap = {}
        for idx, val in enumerate(nums):
            hashmap.setdefault(val, []).append(idx)  # value -> list of indices

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # note: i+1, not i
                x = nums[i]
                y = nums[j]
                req = -(x + y)
                if req in hashmap:
                    # check if any index for `req` is not i and not j
                    valid_indices = [idx for idx in hashmap[req] if idx != i and idx != j]
                    if valid_indices:
                        sum3 = sorted([x, y, req])
                        if sum3 not in final_list:
                            final_list.append(sum3)
        return final_list