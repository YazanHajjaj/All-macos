import scipy.signal
a=[-0.6 ,1.6 ,0.6]
b=[-4 , 3 , 0.6]
r,p,k = scipy.signal.residue(b, a)
print("r0",round(r[0]))
print("r1",round(r[1]))
print("p0",round(p[0]))
print("p1",round(p[1]))
print("k0",round(k[0]))

