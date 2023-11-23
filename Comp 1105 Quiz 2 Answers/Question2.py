# Write a function that reverses a list
# The original list cannot be changed though.

def Q2(orgLs):
    
    ls = orgLs[1:] + orgLs[0:1]
    return ls


# testing the function
print(Q2([2, 3, 5, 7, 11, 13]))
