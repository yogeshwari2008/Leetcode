class Solution(object):
    def isPerfectSquare(self, num):
        g = 0
        while g <= num:
            if g*g<num:
                g+=1
            elif g*g == num:
                return True 
            else:
                return False