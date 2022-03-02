#G#iven a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string. 

#Example 1:
#Input: s = "leetcodeisacommunityforcoders"
#Output: "ltcdscmmntyfrcdrs"

#Example 2:
#Input: s = "aeiou"
#Output: ""

#Solution:

s = "leetcodeisacommunityforcoders"
list1=['a', 'e', 'i', 'o','u']
def removevowels():
    s2 ="".join(i for i in s if i not in list1)
    print(s2)

removevowels()
