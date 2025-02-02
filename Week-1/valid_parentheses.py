class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0 :
            return False

        bracket_stack = []
        close_to_open = {")" : "(", "}" : "{", "]" : "["}

        for bracket in s:
            if bracket in close_to_open:
                if bracket_stack and bracket_stack[-1] == close_to_open[bracket]:
                    bracket_stack.pop()
                else: 
                    return False
            else:
                bracket_stack.append(bracket)

        return True if not bracket_stack else False