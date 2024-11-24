str1="python programming"
char_str={}
for chr in str1:
    if chr in char_str:
        char_str[chr]+=1
    else:
        char_str[chr]=1

print(char_str)