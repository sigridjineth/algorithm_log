# 이진 탐색으로 풀어보는 카카오 2020 가사 검색
from bisect import bisect_left, bisect_right

MAX_WORD_LENGTH = 10001

def solution(words, queries):
    array = [[] for _ in range(MAX_WORD_LENGTH)]
    reversed_array = [[] for _ in range(MAX_WORD_LENGTH)]
    answer = []

    for word in words:
        array[len(word)].append(word) # 리스트 하나를 만들고 단어가 N개인 녀석에 접근하면 N개인 단어들이 모두 나옴
        reversed_array[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입하는 데 이유는 와일드카드가 앞에 나오는 경우에도 고민하기 위함임
    
    # 이진 탐색을 하려면 정렬을 수행해야 함
    for i in range(MAX_WORD_LENGTH):
        array[i].sort() # 하나씩 해당되는 리스트에 접근하여 정렬한다.
        reversed_array[i].sort()

    # 쿼리를 하나씩 확인하며 처리
    for q in queries:
        if (q[0] != "?"): # 접미사에 와일드카드가 붙은 경우를 처리한다
            # 처음은 a요 끝은 z이더라
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else: # 접두사에 있는 경우
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        # 검색된 단어의 개수를 저장
        answer.append(res)
    return answer

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 트라이로 풀어보는 카카오 2020 가사 탐색
class Node:
    def __init__(self):
        self.alpha = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        temp = self.root
        for w in word:
            if temp.alpha.get(w):
                temp = temp.alpha[w]
            else:
                temp.alpha[w] = Node()
                temp = temp.alpha[w]
            temp.count += 1

    # 1. ??를 제외한 queries가 단어와 동일하다.
    # 2. ??를 포함한 queries의 길이가 단어의 길이와 동일하다.
    def search(self, query):
        count = 0
        if (query == ""):
            for val in self.root.alpha.values():
                count += val.count
            return count
        temp = self.root
        for w in query:
            if (temp.alpha.get(w)):
                temp = temp.alpha[w]
                count = temp.count
            else:
                return 0
        return count
    
def solution_2(words, queries):
    # array
    t_a = [Trie() for i in range(10001)]
    # reversed
    r_a = [Trie() for i in range(10001)]

    for word in words:
        t_a[len(word)].insert(word)
        r_a[len(word)].insert(word[::-1])

    answer = [0 for _ in range(len(queries))]
    for (idx, que) in enumerate(queries):
        if (que[0] != "?"):
            s_que = que.split("?")[0]
            answer[idx] = t_a[len(que)].search(s_que)
        else:
            s_que = que.split("?")[-1]
            answer[idx] = r_a[len(que)].search(s_que[::-1])
    return answer
    