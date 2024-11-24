scores={'a': 90,'b':92,'c':100, 'd':83}
max_val=max(scores.values())
#print(max_val)
max_keys=[]
for key,value in scores.items():
    if value==max_val:
        max_keys.append(key)

print(max_keys)

