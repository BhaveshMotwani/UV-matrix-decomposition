# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 17:22:05 2017

@author: bhave
"""
import numpy as np
import math
import sys
f=sys.argv[1]
a=int(sys.argv[2])
b=int(sys.argv[3])
c=int(sys.argv[4])
d=int(sys.argv[5])
file=open(f,'r')

x=np.zeros((a,b))
x[:]=np.NAN
for line in file:
        k=line.split(',')
        x[int(k[0])-1][int(k[1])-1]=int(k[2])
u=np.ones((a,c))
v=np.ones((c,b))
k=np.count_nonzero(~np.isnan(x))
for h in range(d):
    for i in range(a):
        for j in range(c):
            gh=np.dot(u[i],v)
            ad=u[i][j]*v[j]
            gh=gh-ad
            fp=x[i]-gh
            fp=fp*v[j]
            m=v[j]+fp-fp
            jk=np.nansum(fp)/np.nansum(np.square(m))

            u[i][j]=jk

    for i in range(b): 
        for j in range(c): 
            gh=np.dot(u,v[:,i])
            ad=v[j][i]*u[:,j]
            gh=gh-ad
            fp=x[:,i]-gh
            fp=fp*u[:,j]
            m=u[:,j]+fp-fp

            jk=np.nansum(fp)/np.nansum(np.square(m))

            v[j][i]=jk
    #print u,v

    z=np.dot(u,v)
    l=np.square(abs(z-x))
    j=np.nansum(l)
    j=math.sqrt(j/k)
    print "%.4f"%j