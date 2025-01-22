'''Small calculator program I created to solve some math problems'''

from scipy.stats import norm

# Values
mu = 25000  # mean
sigma = 3000  # standard deviation
X_a = 35000 # X-values
X_b = 20000
z_c = 0.99 # z-value

# Propability that X is bigger than limit
def probabilityBigger(value):
    z_a = (value - mu) / sigma
    p_a = 1 - norm.cdf(z_a)
    return p_a



# Propability that X is smaller than limit
def proablilitySmaller(value):
    z_b = (arvo - mu) / sigma
    p_b = norm.cdf(z_b)  
    return p_b



print(todennakoisuusSuurempaa(X_a))
print(todennakoisuusPienempaa(X_b))




