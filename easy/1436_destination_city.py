class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        source = set()
        destination = set()
        for length in paths:
            source.add(length[0])
            destination.add(length[1])
        return list(destination -source)[0]