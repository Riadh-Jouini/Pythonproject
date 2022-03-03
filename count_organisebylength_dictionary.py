#Problem :

#count number of elements separated by whitespace in a list and print the result as a dictionary.

#Exemple:
#input : nums = ['Red lobster', 'blue magic', 'Apple pie','I love Grapes','Jackfruit yo yo','Apple Pay']    
#Output : {'Red lobster': 2, 'blue magic': 2, 'Apple pie': 2, 'I love Grapes': 3, 'Jackfruit yo yo': 3, 'Apple Pay': 2}     

# Solution: 

from collections import Counter
nums = ['Red lobster', 'blue magic', 'Apple pie','I love Grapes','Jackfruit yo yo','Apple Pay']

nums_low = nums
count=dict()
for i in nums:
    dict2={}
    count[i]=count.get(i, 0) + 1
    for key, value in count.items():
        key_low=key.lower()
        key_low_split = key_low.split(" ")
        len_key_low_split = len(key_low_split)
    #print(f"[{key} : {len_key_low_split}]")
        dict2[key] = len_key_low_split
print(dict2)
