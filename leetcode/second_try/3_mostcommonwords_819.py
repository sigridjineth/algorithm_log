import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = []
        for word in re.sub(r'[^\w]', ' ', paragraph).lower().split():
            if word not in banned:
                words.append(word)
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
