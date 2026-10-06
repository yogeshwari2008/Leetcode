class Solution(object):
    def sortPeople(self, names, heights):
        h=sorted(heights)
        a=[]
        h=h[::-1]
        for i in h:
            a.append(names[heights.index(i)])
        return a       