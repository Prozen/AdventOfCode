s = "1113122113"
for i in range(50):
    result=""
    current =s[0]
    count = 0
    for c in s:
        if c == current:
            count +=1
        else:
            result+=str(count)
            result+=current
            count =1
            current =c
    result+=str(count)
    result+=current
    s= result
print(len(result))
