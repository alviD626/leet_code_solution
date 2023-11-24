class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        height_dict = dict(zip(heights,names))
        names.clear()
        for key in sorted(height_dict.key(),reverse=True):
            names.append(height_dict[key])
        return names