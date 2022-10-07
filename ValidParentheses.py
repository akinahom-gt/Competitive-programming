class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        leftSymbols = []
    for c in s:
        if c in ['(', '{', '[']:
            leftSymbols.append(c)
        elif c == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
            leftSymbols.pop()
        elif c == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
            leftSymbols.pop()
        elif c == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
            leftSymbols.pop()
        else:
    return False
    return leftSymbols == []
