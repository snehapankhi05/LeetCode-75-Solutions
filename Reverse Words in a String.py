class Solution(object):
    def reverseWords(self, s):
        word=s.split()
        print(word)
        res=""

        for i in range(len(word)):
            res=word[i]+" "+res
        return res.strip()
        
