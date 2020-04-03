import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

fig  =plt.figure()
ax = plt.axes()

x = np.linspace(0,10,1000)
### two ways to plot

# ax.plot(x,np.sin(x))
# or
# plt.plot(x,np.sin(x))
# plt.plot(x,np.cos(x))

### Line Colors
# plt.plot(x,np.sin(x),color='blue')
# plt.plot(x,np.cos(x), color='#ffcc00')

### Line Styles
# plt.plot(x,x+1,linestyle='dashed')
# plt.plot(x,x+2,linestyle='dashdot')
# plt.plot(x,x+3,linestyle=':')

### color and style applied together

# plt.plot(x,x+5,'--g')

### titles
# plt.title(" A Sine Curve")
# plt.xlabel("x")
# plt.ylabel("sin(x)")


plt.plot(x, np.sin(x),"-g",label='sin(x)')
plt.plot(x, np.cos(x),":b",label='cos(x)')

# adjusting the plots
# 1. by setting axis limits like :- plt.xlim(10,0)
# 2. plt.axis('tight') to have tight bounds
# as follows
plt.axis('equal')

plt.legend()
plt.show()




