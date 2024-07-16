def long(s1,s2):
    min_len=min(len(s1),len(s2))
    #taking a empty string res
    res=""
    
    for i in range(min_len):
        if s1[i]==s2[i]:
            #This is how we add elemnt to a empty string         
            res += s1[i]
        else:
            break
    return res
string1=input('Enter the first input :')
string2=input('Enter the second input :')
result=long(string1,string2)
print(f'The longer common prefix {result}')