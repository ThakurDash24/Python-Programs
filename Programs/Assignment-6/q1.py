def solution(head,leg):
    for chicken in range(head+1):
        rabbit=head-chicken
        if (2*chicken + 4*rabbit == leg):
           return chicken,rabbit
    return None , None
head=35
leg=94

chicken , rabbits = solution(head,leg)
if chicken is None and rabbits is None :
    print('No Solution Found')
else :
    print(f'Total Number of chickens are {chicken}')
    print(f'Total number of rabbits are {rabbits}')
