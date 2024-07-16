def count(votes):
    vote_count={}
    for vote in votes:
        if vote in vote_count:
            vote_count[vote]+= 1
        else:
            vote_count[vote]=1
    print(vote_count)
    winner = max(vote_count , key=vote_count.get)
    return winner
votes=[]
n=int(input('Total number of votes :'))
for i in range(n):
    votes.append(input('Vote:'))
winner=count(votes)
print(f'The winner is {winner}')