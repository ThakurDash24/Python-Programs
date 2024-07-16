A=[]
n=int(input('Enter the size of the list :'))
for i in range(n):
  ele=int(input(f'Enter the element-{i+1} for the list :'))
  A.append(ele)
lar=A[0]
for i in range(n):
  if(lar<A[i]):
    lar=A[i]
    pos=i  
print(f'The largest one is {lar} present at {i+1}')