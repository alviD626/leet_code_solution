class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        return " ".join([word.lower() if len(word)<3 else word.title() for word in title.split()])