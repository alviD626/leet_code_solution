class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # solution1
        # lo, hi = 0, x
        # while lo<=hi:
        #     mid = (lo+hi)//2
        #     if mid*mid<x:
        #         hi = mid - 1
        #     elif mid*mid>x:
        #         lo = mid + 1
        #     else:
        #         return mid
        
        # Solution2
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1