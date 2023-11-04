#This is a program to call all the keys of the nested dictionaries.

test = {"d":2,"f":{"l":3}}

total = []
for s in test.keys():
    total.append(s)
    if isinstance(test[s],dict):
        for x in test[s].keys():
            total.append(x)
print(tuple(total))
