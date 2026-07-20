class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # the key is the unique integer 
        # value is the times it appears 
        counts={}
        for num in nums:
            counts[num] = counts.get(num,0)+1
        sorted_items = sorted(counts.items(), key = lambda pair:pair[1], reverse=True)
        
        return [num for num,freq in sorted_items[:k]]
