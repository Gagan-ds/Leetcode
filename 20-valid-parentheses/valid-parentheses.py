class Solution:
    def isValid(self, s: str) -> bool:
        open_brac = ["(","[","{"]
        close_brac = {")":"(","]":"[","}":"{"}
        stack = []
        for b in s:
            if b in open_brac:
                stack.append(b)
            elif len(stack)>0:
                if close_brac[b] == stack[-1]:
                    stack.pop(-1)
                else:
                    stack.append(b)
            else:
                stack.append(b)
        # print(stack)
        if len(stack)==0:
            return True
        else:
            return False       