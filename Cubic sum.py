#Cubic sum:-

def isCubicSumExist(A, N):
    max_val = max(A)
    cubes = set()
    limit= int(max_val ** (1/3))+1
    for x in range(1,limit):
        cubes.add(x ** 3)
    def is_good_integer(z):
        for x in cubes:
            if (z - x) in cubes:
                return True
        return False
    count =0
    for z in A:
        if is_good_integer(z):
            count += 1
    return count
N =int(input())
A=list(map(int, input().split()))
output= isCubicSumExist(A, N)
print(output)


#i/p:- 3
#      35 9 1
#o/p:  2
