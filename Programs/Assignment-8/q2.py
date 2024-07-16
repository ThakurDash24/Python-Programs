n=int(input('Enter the number of product :'))
prod_qty=[]
prices=[]
res=[]
for i in range(n):
    prod_qty.append(int(input('Enter the Quantities :')))
    prices.append(float(input('Enter the corresponding price :')))
res=[prod_qty[i]*prices[i] for i in range(n)]
total=sum(res)
print(f'The total would be {total}')
    
    
    