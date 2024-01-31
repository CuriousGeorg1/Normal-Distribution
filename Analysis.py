'''Small calculator program I created to solve some math problems'''

from scipy.stats import norm

# Arvot
mu = 25000  # mean
sigma = 3000  # standard deviation
X_a = 35000 # X-values
X_b = 20000
z_c = 0.99 # z-value

# Propability that X is bigger than limit
def todennakoisuusSuurempaa(arvo):
    z_a = (arvo - mu) / sigma
    p_a = 1 - norm.cdf(z_a)  # Todennäköisyys, että z-arvo on suurempi kuin z_a
    return p_a



# Propability that X is smaller than limit
def todennakoisuusPienempaa(arvo):
    z_b = (arvo - mu) / sigma
    p_b = norm.cdf(z_b)  # Todennäköisyys, että z-arvo on pienempi kuin z_b
    return p_b



# percentage that exceeds given limit
def overLimit(raja):
    z_c = norm.ppf(0.99)
    X_c = z_c * sigma + mu  # Selvitetään X arvo
    return X_c

print(todennakoisuusSuurempaa(X_a))
print(todennakoisuusPienempaa(X_b))
print(overLimit(z_c))



