from itertools import combinations
def PlayList(airTime, songs, n):
    if songs is None or n< 3:
        return -1
    count=0
    for combo in combinations(songs, 3):
        if sum(combo) == airTime:
            count +=1
    return count
airTime = int(input())
n=int(input())
songs=[]
print()
songs = list(map(int,input().split()))
output=PlayList(airTime, songs,n)
print(output)

#i/p:-40
#     8
#     7 14 21 19 17 2 29 5
#the playlist that sum 40 are
# {14,21,5},{7,14,19},{21,17,2}
