class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = self.generate_count(s)
            groups.setdefault(key, []).append(s)
        return list(groups.values())

    def generate_count(self, s):
        counts = [0] * 26
        for x in s:
            i = ord(x) - ord("a")
            counts[i] += 1
        return tuple(counts)