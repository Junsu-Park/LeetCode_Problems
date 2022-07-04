from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        group = defaultdict(list)
        for s in strs:
            s_ = ''.join(sorted(s))
            group[s_].append(s)
        return list(group.values())