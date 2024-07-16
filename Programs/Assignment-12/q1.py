import random
dice_counts={i:0 for i in range (1,7)}
for _ in range(500):
    roll=random.randint(1,6)
    dice_counts[roll]+=1
for face,count in dice_counts.items():
    print(f"num {face} appeared {count} times")

