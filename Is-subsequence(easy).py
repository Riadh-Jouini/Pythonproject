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