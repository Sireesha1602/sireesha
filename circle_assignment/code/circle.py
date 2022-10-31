#python libraries for math and graphics


import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import random

import sys
sys.path.insert(0,'/home/sireesha/Desktop/CoordGeo')

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if 

#Given Points
A = np.array(([2,4]))
B = np.array((0,1))
W = np.array((-1,0))
m = np.array((-1,-4))
#Finding Center
At = 2*A.T
Bt = 2*B.T
mt = m.T
i = -np.linalg.norm(A)**2
j = -np.linalg.norm(B)**2
k = -m@A
S = np.block([[At,1],[Bt,1],[mt,0]])
#S = np.array([[At[0],At[1],1],[Bt[0],Bt[1],1],[mt[0],mt[1],0]])


T = np.block([i,j,k])
P = LA.solve(S,T)
print("Solution vector p=",P)
u=np.array((P[0],P[1]))
print("u =",u)
#C = np.array(((-P[0],-round(P[1],2))))
C = np.block(-(u))
print("center = ",C)
f=P[2]
print("f = ",f)

#generating the circle
r=5.36
x_circ=circ_gen(C,r)


tri_coords=np.vstack((C,B)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels=['C','B(0,1)']
for i,txt in enumerate(vert_labels):
   plt.annotate(txt,#this is the text
                (tri_coords[0,i], tri_coords[1,i]), #this is the point to label
                textcoords="offset points", #how to position the text
                xytext=(0,10), # distance from text to points (x,y)
                ha='center') #horizontal alignment can be left.right or center
              
              
tri_coords=np.vstack((C,A)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels=['C','A(2,4)']
for i,txt in enumerate(vert_labels):
   plt.annotate(txt,#this is the text
                (tri_coords[0,i], tri_coords[1,i]), #this is the point to label
                textcoords="offset points", #how to position the text
                xytext=(0,10), # distance from text to points (x,y)
                ha='center') #horizontal alignment can be left.right or center
                         

#plotting the circle 
plt.axhline(0,color='k')
plt.axvline(0,color='k')
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')

#plotting the curve
x=np.linspace(-2,2,100)
y=x**2
plt.plot(x,y)


#generate the radius
x_CB=line_gen(C,B)
plt.plot(x_CB[0,:],x_CB[1,:],label='$Radius$')
x_CA=line_gen(C,A)
plt.plot(x_CA[0,:],x_CA[1,:])


#labelling the coordinates

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() #minor
plt.axis('equal')

#if using termux
#plt.savefig('#path')
#subprocess.run(shlex.split('#commamd to open file'))
#else

plt.show()




