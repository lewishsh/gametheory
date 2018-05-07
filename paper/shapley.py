import numpy as np
import itertools

v = {():0, (1,):24, (2,):48, (3,):24, (4,):72, (1,2):96, (1,3):0, (1,4):120,
     (2,3):144, (2,4):0, (3,4):0, (1,2,3):0, (1,2,4):0, (1,3,4):168,
     (2,3,4):0, (1,2,3,4):240}
permutations = list(itertools.permutations([1,2,3,4]))
shapley = [0,0,0,0]

for permutation in permutations:
    S = []
    for i in permutation:
        S_old = S[:]
        S += [i]
        S.sort()
        shapley[i-1] += v[tuple(S)] - v[tuple(S_old)]

shapley = np.array(shapley)/24
print(shapley)

        
        
