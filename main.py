# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

"""
UPER:
U:
    > Given two strings
    > They may or may not be the same length
    > How many deletions must be done to make them anagrams?
    > You can delete characters from both strings
    > Return the number of deletions

P:
    > Check how many matching letters with a cache
        > In cache: key:letter and value:# times found


"""

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    counta = 0
    countb = 0
    cache = {}

    for n in a:
        counta += 1
        
        if n in cache:
            cache[n] += 1
        else:
            cache[n] = 1
    
    for x in b:
        if x not in cache:
            countb += 1
        elif cache[x] == 0:
            countb += 1
        else:
            cache[x] -= 1
            counta -= 1
    
    return counta + countb