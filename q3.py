import numpy as np
import math

# Analytical solution
n = np.linspace(2, 15, 14)
n = range(2, 16, 1)

def analytical_V(n):
    gamma_val = math.gamma((n/2) + 1)
    
    return (np.pi ** (n/2))/ gamma_val

analytical_volume = np.zeros(len(n))
for i in range(len(n)):
    print("The analytical solution for ", n[i], "dimensions is", analytical_V(n[i]))
    analytical_volume[i] = analytical_V(n[i])


# Monte carlo attempt
n_pts = 1000000

cnt = np.zeros(len(n))
volume = np.zeros(len(n))

# for each number of dimensions
for i in range(0, len(n)):
    # create two dimension array of n x n_pts length
    dimensions = np.zeros([int(n[i]), n_pts])
    # generate list of random numbers for each dimension
    for j in range(len(dimensions)):
        dimensions[j] = np.random.random(n_pts)
        
    # loop over every row
    for k in range(n_pts):
        r_squared = 0
        # for each column add the dimension squared
        for l in range(int(n[i])):
            r_squared += dimensions[l, k] ** 2
        
        # if r squared for that row is less than unit value it is in circle
        if(r_squared < 1.0):
            cnt[i] += 1

# for each dimension we are finding value of
# calc volume by cnt divided by total points
# multiplied by number of positive and negative axes 2^n
for i in range(len(volume)):
    volume[i] = cnt[i]/n_pts * (2**n[i])
    print("The monte carlo solution for ", n[i], "dimensions is", volume[i])

print("N | Analytical Solution | Monte Carlo solution")
for i in range(len(volume)):
    print(n[i], "|", analytical_volume[i], "|", volume[i])
