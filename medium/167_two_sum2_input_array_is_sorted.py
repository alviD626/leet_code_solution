class Solution(object):
    def twoSum(self, numbers, target):
        if len(numbers) == 0:
            return [-1]
        else:
            start = 0
            end = len(numbers) - 1
            while start < end :
                cur_sum = numbers[start] + numbers[end]
                if cur_sum == target:
                    return [start+1,end+1]
                elif cur_sum < target:
                    start += 1
                elif cur_sum > target:
                    end -= 1
            return [-1]