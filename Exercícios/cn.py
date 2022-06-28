
def gaussElimin(a, b):
    n = len(b)
  # Elimination Phase
    for k in range(0, n-1):
        for i in range(k+1, n):
           if a[i, k] != 0.0:
               lam = a[i, k]/a[k, k]
               a[i, k+1:n] = a[i, k+1:n] - lam*a[k, k+1:n]
               b[i] = b[i] - lam*b[k]
        
    for k in range(0, n-1):
        for i in range(k+1, n):
            print(f'[a[k][i]]', end = '')
        print('\n')
                
    
# Back substitution
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k+1:n], b[k+1:n]))/a[k, k]
    return b

z = array([[-1.0, 3.0, 5.0, 2.0],
             [1.0, 9.0, 8.0, 4.0],
             [0.0, 1.0, 0.0, 1.0],
             [2.0, 1.0, 1.0, -1.0]])

k = array([[10.0, 15.0, 2.0, -3.0]])

x = gaussElimin(z, k[0])

print('x = \n', x)