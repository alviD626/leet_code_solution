class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        #solution1
        maxwealth = 0
        for i in range(len(accounts)):
            totalwealth = sum(accounts[i])
            maxwealth = max(maxwealth,totalwealth)
        return maxwealth
        
        #solution2
        # return max(sum(i) for i in accounts)
        
        #solution3
        # return max(map(sum,accounts))