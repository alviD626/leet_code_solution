class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        # max_len = 0
        # for sentence in sentences:
        #     split_list = sentence.split()
        #     size_of_split_list = len(split_list)
        #     if size_of_split_list > max_len:
        #         max_len = size_of_split_list
        # return max_len
        count = 0
        for i in sentences:
            c = len(i.split())
            if(c>count):
                count = c
        return count
    

sentence = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
solution = Solution()
result = solution.mostWordsFound(sentence)
print(result)