import matplotlib.pyplot as plt
import numpy as np

fig ,ax = plt.subplots()
ax.plot([1,2,3,4],[1,4,2,3])

# this start a event loop that looks for all currently active figure objects and
# opens one or more window that displays your figure or figures
# should be used only once per python session
# It is not always required command. Required in case of script, not neccessary in case
#  notebook  and shell

plt.show()




