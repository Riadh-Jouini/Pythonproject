from collections import Counter
nums = ['Red lobster', 'blue Jay Z', 'Apple pie','Grapes mah nigga','Jackfruit yoyo','Apple Pay']

nums_low = nums
count=dict()
for i in nums:
    list1 = []
    list2 = []
    list3 = list1 + list2
    dict2={}
    count[i]=count.get(i, 0) + 1
    for key, value in count.items():
        key_low=key.lower()
        key_low_split = key_low.split(" ")
        len_key_low_split = len(key_low_split)
    #print(f"[{key} : {len_key_low_split}]")
        dict2[key] = len_key_low_split
print(dict2)
