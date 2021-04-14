import numpy as np
#rejection sampling
simlen=int(1e7)
def rng_xpy(n, rng=None, chunk_size=1024):
    rng = np.random.default_rng(rng)
    cot=0
    rvs = []
    n_drawn = 0
    while n_drawn < n:
        # Draw numbers from U(0, 1) for x, y, and z
        # We draw numbers in chunks for efficiency
        x, y,z= rng.random((3, chunk_size))
       
        # Scale z to U(0,2)
        z = z*2
        
        # We only want to use (x, y) values when z is less than x+y(pdf value)
        pz = z <= (x + y) #as x+y is the value of the pdf. 
        
        xy = np.column_stack([x, y])[pz]# stores the cases for which pz is true
        #print(xy)
        #print(z)
        
        rvs.append(xy)
        n_drawn += len(xy)
        
    # Because we draw in chunks, we probably drew too many.cutting down the array to match required number of values
    
    xy = np.concatenate(rvs, axis=0)[:n]
 
    return xy
    
count=0
problist=rng_xpy(simlen)
for a in range(0,simlen):
  if problist[a][0]+problist[a][1]<=1:
    count=count+1
print("{} is the simulated probability and {} is the theoretical probability".format((count/simlen),1/3 ))