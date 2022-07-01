from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        group = defaultdict(list)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for s in strs:
            a_dict = {i:0 for i in alphabet}
            for el in s:
                a_dict[el] += 1
            key = ''
            for k,v in a_dict.items():
                key += str(k) + str(v)
            group[key].append(s)
        return list(group.values())