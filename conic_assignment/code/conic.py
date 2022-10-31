
#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                 				#for path to external scripts
sys.path.insert(0,'/home/sireesha/Desktop/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

#Input parameters


V1 = np.matrix('16,0;0,25')
V2 = np.matrix('-16,0;0,9')	
l1,P = np.linalg.eigh(V1)
l2,p = np.linalg.eigh(V2)		#l-eigen_values & v-eigen_vector
f1 = -V1[0,0]*V1[1,1]
f2 = -V2[0,0]*V2[1,1]

l11 = l1[0]	#lambda_1
l12 = l2[1]
l21 = l2[0]
l22 = l2[1]	#lambda_2

P1 = P[0].T	#eigenvector_1
P2 = P[1].T	#eigenvector_2

e1 = np.sqrt(1-(l11/l12))			#eccentricity
e2 = np.sqrt(1-(l21/l22))
n1 = np.sqrt(l12)*P1			#normal to diretrix
n2 = np.sqrt(l22)*P1
k1 = np.sqrt(-(l12*((e1*e1)-1)*(-l12*f1)))/(l12*e1*((e1*e1)-1))	#constant
k2 = np.sqrt(-(l22*((e2*e2)-1)*(-l22*f2)))/(l12*e2*((e2*e2)-1))
F1 = (k1*e1*e1*n1)/l12   #focus of ellipse
F2=(k2*e2*e2*n2)/l22	#Focus of hyperbola
print ('The focus of hyperbola is=',F2)




A = np.array([-np.sqrt(l11),0])
B = np.array([np.sqrt(l11),0])
C = np.array([0,np.sqrt(l12)])
D = np.array([0,-np.sqrt(l12)])
m = float(F1[0])
F1 = np.array([m,0])


#Generating the ellipse
x_ellipse = ellipse_gen(np.sqrt(l11),np.sqrt(l12))

#Plotting the ellipse
plt.plot(x_ellipse[0,:],x_ellipse[1,:],label='$Ellipse$')

#Generating the hyperbola
def hyper_gen(y):
        x=np.sqrt((l22*y**2+f2)/(-l21))
        return x
len=100
y=np.linspace(-7,7,len)
x=hyper_gen(y)
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')
        
#plotting the hyperbola
plt.plot(x,y,label='Hyperbola')
plt.plot(-x,y)



#Generating all lines
xAB = line_gen(A,B)
xCD = line_gen(C,D)
xCF = line_gen(C,F1)

#Plotting all lines
plt.plot(xAB[0,:],xAB[1,:],label='Major Axis')
plt.plot(xCD[0,:],xCD[1,:],label='Minor Axis')



#Labeling the coordinates
tri_coords = np.vstack((A,B,C,D,F1)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','F1']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-5,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='upper left')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('/sdcard/FWC/Matrices/Conic/conicp.pdf')
#subprocess.run(shlex.split("termux-open '/sdcard/FWC/Matrices/Conic/conicp.pdf'"))
#else
plt.show()
