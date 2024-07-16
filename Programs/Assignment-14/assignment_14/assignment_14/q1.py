f=open('Assignment-14/assignment_14/assignment_14/sowpods.txt','r')
words=f.readlines()
words=[word.strip() for word in words]
words_wid_uu=[word for word in words if 'UU' in word]
for word in words_wid_uu:
    print(word)
f.close()