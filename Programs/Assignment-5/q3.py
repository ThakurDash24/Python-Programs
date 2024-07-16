def extraction(list):
    unique=[]
    items=list.split(',')
    for item in items:
        stripped=item.strip()
        if stripped not in unique:
            unique.append(stripped)
    return unique
list=input('Enter the comma-separated list :')
res=extraction(list)
print(res)