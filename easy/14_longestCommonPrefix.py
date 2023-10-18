# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
     
a =["my","myme","myis","mystakim"]
# b = sorted(a)
# print(b)

# first = b[0]
# print(first)

# last = b[-1]
# print(last)

# c = min(len(first),len(last))
# print(c)

# ans = ""

# for i in range(min(len(first),len(last))):
#     if first[i] != last[i]:
#         print(ans)
#     ans += first[i]
# print(ans)

pre = a[0]
print(pre)
for i in a:
    while not i.startswith(pre):
        pre =pre[:-1]
        print(pre)
print(pre)