class Solution:
    def reverse(self, x: int) -> int:
        new_num = 0
        count = 0
        z = False
        if x<0:
            x = abs(x)
            z = True
        while x>0:
            num = x%10
            new_num = new_num*10+num
            x = x//10
        if z is True:
            if (-2**31)<new_num<(2**31)-1:
                return (0-new_num)
            else:
                return 0
        if (-2**31)<new_num<(2**31)-1:
            return new_num
        else:
            return 0
        