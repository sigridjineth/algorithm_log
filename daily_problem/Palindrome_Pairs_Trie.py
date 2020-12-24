# Palindrome Pairs LEETCODE 336
# Trie 자료구조를 이용한 팰린드롬 페어 문제
import collections
from typing import List

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []
        self.val = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]
    
    # 단어를 삽입해야 한다. 팰린드롬을 판별하는 문제이므로 거꾸로 넣어보면 된다.
    # 예를 들어 cbbcd를 넣을 때는 d->c->b->b->c 순서로 트라이 노드가 구성된다.
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if (self.is_palindrome(word[0:len(word) -i])):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
            node.val = char
        node.word_id = index
    
    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            # 판별 로직: 탐색 중간에 word_id가 있고 나머지 문자가 팰린드롬인 경우
            # 입력값을 문자 단위로 확인해 나가다가 해당 노드의 word_id가 -1이 아닌 경우, 나머지 문자가 팰린드롬인 경우
            # ex) dcbc + d -> dcbc는 먼저 d부터 탐색하다가 d의 word_id가 -1이 아니므로 cbc를 팰린드롬 여부를 확인한다.
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
        
        # 판별 로직: 끝까지 탐색했을 때 word_id가 있는 경우 해당 word_id를 팰린드롬으로 판별한다.
        # 단어를 뒤집어서 구축한 트라이이기 때문에 입력값은 순서대로 탐색하다가, 끝나는 지점의 word_id 값이 -1이 아니면
        # 현재 인덱스 index와 해당 word_id는 팰린드롬으로 판단할 수 있다.
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
        
        # 판별 로직: 끝까지 탐색했을 때 palindrome_word_ids가 있는 경우
        # 트라이 삽입 중에 남아있는 단어가 팰린드롬이라면 미리 팰린드롬 여부를 세팅한다. 이게 제일 이해가 어려웠는데..
        # 예를 들어 cbbc는 단어 자체가 팰린드롬이므로 루트에 바로 입력값의 인덱스를 삽입할 수 있다.
        # 그 이후에 word[0:len(word)-i] 형태로 단어에서 문자 수를 계속 줄여나가며 팰린드롬 여부를 체크한다.
        # 문자가 하나만 남게 될 때는 항상 팰린드롬이므로 인덱스를 마지막에 세팅한다. 이 때는 word_id 바로 앞 노드가 된다.
        for node.palindrome_word_id in node.palindrome_word_ids:
            result.append([index, node.palindrome_word_id])
        return result

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(i, word)
        results = []
        for i, word in enumerate(words):
            # Python에서 extend는 iterable한 elements를 모두 list에 넣는 것을 의미한다.
            results.extend(trie.search(i, word))
        return results

words = ['d', 'cbbcd', 'dcbb', 'dcbc', 'cbbc', 'bbcd']
print(Solution().palindromePairs(words))