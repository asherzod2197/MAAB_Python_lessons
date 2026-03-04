import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# ---------------- 1 Basic Plot ----------------

x = np.linspace(-10,10,200)
y = x**2 - 4*x + 4

plt.figure()
plt.plot(x,y)
plt.title("f(x) = x^2 - 4x + 4")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()



# ---------------- 2 Sine Cosine ----------------

x = np.linspace(0,2*np.pi,200)

plt.figure()

plt.plot(x,np.sin(x),'r--o',label="sin(x)")
plt.plot(x,np.cos(x),'b-^',label="cos(x)")

plt.title("Sine and Cosine")
plt.xlabel("x")
plt.ylabel("value")
plt.legend()

plt.show()



# ---------------- 3 Subplots ----------------

x = np.linspace(0,5,200)

fig,ax = plt.subplots(2,2)

ax[0,0].plot(x,x**3,'r')
ax[0,0].set_title("x^3")
ax[0,0].set_xlabel("x")
ax[0,0].set_ylabel("y")


ax[0,1].plot(x,np.sin(x),'b')
ax[0,1].set_title("sin(x)")
ax[0,1].set_xlabel("x")
ax[0,1].set_ylabel("y")


ax[1,0].plot(x,np.exp(x),'g')
ax[1,0].set_title("e^x")
ax[1,0].set_xlabel("x")
ax[1,0].set_ylabel("y")


ax[1,1].plot(x,np.log(x+1),'m')
ax[1,1].set_title("log(x+1)")
ax[1,1].set_xlabel("x")
ax[1,1].set_ylabel("y")

plt.tight_layout()
plt.show()



# ---------------- 4 Scatter Plot ----------------

x = np.random.uniform(0,10,100)
y = np.random.uniform(0,10,100)

plt.figure()

plt.scatter(x,y,c=y,marker='o')

plt.title("Random Scatter")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid()

plt.show()



# ---------------- 5 Histogram ----------------

data = np.random.normal(0,1,1000)

plt.figure()

plt.hist(data,bins=30,alpha=0.6)

plt.title("Histogram Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()



# ---------------- 6 3D Plot ----------------

x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)

X,Y = np.meshgrid(x,y)

Z = np.cos(X**2 + Y**2)

fig = plt.figure()

ax = fig.add_subplot(111,projection='3d')

surf = ax.plot_surface(X,Y,Z,cmap='viridis')

fig.colorbar(surf)

ax.set_title("3D Surface")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()



# ---------------- 7 Bar Chart ----------------

products = ['Product A','Product B','Product C','Product D','Product E']

sales = [200,150,250,175,225]

plt.figure()

plt.bar(products,sales,
        color=['red','blue','green','orange','purple'])

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()



# ---------------- 8 Stacked Bar ----------------

labels = ['T1','T2','T3','T4']

A = [10,20,30,40]
B = [15,25,20,30]
C = [5,10,15,20]

plt.figure()

plt.bar(labels,A,label="Category A")
plt.bar(labels,B,bottom=A,label="Category B")

bottom2 = np.array(A)+np.array(B)

plt.bar(labels,C,bottom=bottom2,label="Category C")

plt.title("Stacked Bar Chart")
plt.xlabel("Time")
plt.ylabel("Values")

plt.legend()

plt.show()