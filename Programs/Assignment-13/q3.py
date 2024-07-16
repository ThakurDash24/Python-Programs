def sort_key(sublist):
    return sublist[0]
def sort_by_value(input):
    sorted_list=sorted(input,key=sort_key)
    return sorted_list
input=[[5, 7], [9, 11], [7, 3], [0, 12]]
sorted_output=sort_by_value(input)
print("Input :",input)
print("Sorted one :",sorted_output)

