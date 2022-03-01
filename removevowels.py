s = "leetcodeisacommunityforcoders"
list1=['a', 'e', 'i', 'o','u']
def removevowels():
    s2 ="".join(i for i in s if i not in list1)
    print(s2)

removevowels()