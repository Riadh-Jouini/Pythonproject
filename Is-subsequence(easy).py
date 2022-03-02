#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

#A subsequ#ence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

#Example 1:

#Input: s = "abc", t = "ahbgdc"
#Output: true
#Example 2:

#Input: s = "axc", t = "ahbgdc"
#Output: false

#Solution:

input1 = "abc"
input2 = "bhdcea"
x = 0
y = "".join(i for i in input2 if i in input1)

if y == input1:
    print(True)
    print(y)
else:
    print(False)
    print(y)
