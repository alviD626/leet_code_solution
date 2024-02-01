class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        m = -1
        i = len(arr)-1
        while i>=0:
            temp = arr[i]
            arr[i] = m
            if temp>m:
                m = temp-m
            i -= 1
        return arr
        class Solution(object):
        # def replaceElements(self, arr):
        
        #     me,arr[-1] = arr[-1],-1
            
        #     for i in range(len(arr)-2,-1,-1):
        #         arr[i],me = me,max(me,arr[i])
                
        #     return arr