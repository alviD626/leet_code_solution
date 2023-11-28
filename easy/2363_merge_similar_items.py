class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        merged = defaultdict(int)
        
        for value,weight in items1+items2:
            merged[value] += weight
        
        return sorted(merged.items())