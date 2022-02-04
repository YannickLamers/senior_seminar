#exercise_3.py

import numlib as nl

m=2**64
a=123456789

R = nl.Zmod(m)
d=nl.gcd(a,m)

print('gcd(a,m) =' , d)
print( 'introduce an integer: ')

x = int(input())
k = R(x)
b = a*k

r = b%d

print( 'For a =', a, ', m =', m, ',d =', d, 'a*x(mod(m))% d=', r)

