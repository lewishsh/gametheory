from scipy.special import binom as bn
from math import factorial as f
import numpy as np



sum = 0
for k in range(4,11):
    sum += bn(10, k)*f(4+k)*f(15-(4+k)-1)/f(15)

print(sum)

print((1 - 5*sum)/10)
