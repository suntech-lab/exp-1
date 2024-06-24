def sigma(y):
    if y==1:
        return y
    return y*sigma(y-1)

def permutations(n, r):
    return sigma(n)//sigma(n-r)

n=6
r=4

result_permutations = permutations(n, r)
print(result_permutations)