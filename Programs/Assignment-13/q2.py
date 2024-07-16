def transfor(input):
    upper=''.join(map(str.upper,input))
    lower=''.join(map(str.lower,input))
    return upper , lower
input=input('Enter the string')
upper,lower=transfor(input)
print("Orignal :",input)
print("Upper case:",upper)
print("Lower case:",lower)