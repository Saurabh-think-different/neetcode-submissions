class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        group = defaultdict(list)

        for str in strs:
            prev = str
            str = tuple(sorted(str))
            group[str].append(prev)
        
        return list(group.values())