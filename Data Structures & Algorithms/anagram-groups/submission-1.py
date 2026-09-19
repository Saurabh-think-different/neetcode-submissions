class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        group = defaultdict(list)

        for str in strs:
            count = [0] * 26
            for i in str:
                count[ord(i)-ord('a')] += 1
            s = tuple(count)
            group[s].append(str)
        
        return list(group.values())