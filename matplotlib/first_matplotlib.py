import matplotlib.pyplot as plt
import numpy as np

#MATPLOTLIP PLOTTING
#Single points
# xpoint = np.array([1, 5])
# ypoint = np.array([4, 20])

#Multiple points
# ypoint = np.array([20, 12, 4])
# xpoint = np.array([1, 3, 5])
# plt.plot(xpoint, ypoint)
# plt.show()


#MATPLOTLIB MARKERS
y_axis = np.array([3, 8, 1, 10])
plt.plot(y_axis, '*:b', ms=10, mec='c', mfc='g')
plt.show()