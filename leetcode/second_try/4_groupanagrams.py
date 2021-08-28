# Group Anagrams Q49
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            identifier = str("".join(sorted(word)))
            anagrams[identifier].append(word)
        return anagrams.values()
