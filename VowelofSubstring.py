class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
    n = len(word)
    res = 0
    for i in range(n):
		if word[i] in "aeiou":
			res += (i + 1) * (n - i)
    return res
