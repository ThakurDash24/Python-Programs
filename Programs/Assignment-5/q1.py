num_list=[]
n=int(input('Enter the siz of the list :'))
for x in range(n):
    ele=input(f'Enter the element-{x+1}=')
    if(ele>=0):
        num_list.append(ele)
    else :
        print('Enter a valid input')
num=input('Enter the number you want to check')
if num in num_list:
    print('The element is present')
else :
    print('The eement is not present in the list')
