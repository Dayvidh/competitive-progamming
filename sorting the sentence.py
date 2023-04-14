class Solution:
    def sortSentence(self, s: str) -> str:
        word_list = s.split()
        res = ''
        for i in range(0, 10):
            for words in word_list:
                if words[-1] == str(i):
                    res += " " + words[:-1]
        return res.strip()
