def find_substring(string,substring):
    len_sub=len(substring)
    for i in range(len(string)-len_sub+1):
        if string[i:i+len_sub]==substring:
            return True
    return False
main='Hello There , how are you doing ?'
sub= 'ng'
if (find_substring(main,sub)):
    print(f'Substring `{sub}` found in the main string ')
else:
  print(f'Substring `{sub}` is not present in the string')