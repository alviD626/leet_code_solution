class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        d = {"type":0, "color":1, "name": 2}
        c = 0
        Index = d[ruleKey]
        for item in items:
            if item[Index] == ruleValue:
                c+=1
        return c