class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [letter for letter in s if letter.isalpha()]
        answer = []
        for each in s:
            if each.isalpha():
                answer.append(letters.pop())
            else:
                answer.append(each)
        return "".join(answer)
