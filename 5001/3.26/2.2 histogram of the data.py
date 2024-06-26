import numpy as np
import matplotlib.pyplot as plt

# data set: weight of car rearview mirror components
data = [
    3.968, 3.534, 4.03, 3.912, 3.572, 4.014, 3.682, 3.608, 3.669, 3.705,
    4.02, 3.588, 3.94, 3.871, 3.74, 3.711, 3.645, 3.977, 3.88, 3.948,
    3.55, 3.796, 3.65, 3.667, 3.799, 4.010, 3.70, 3.642, 3.68, 3.554,
    4.02, 4.079, 3.621, 3.575, 3.71, 4.017, 4.08, 3.660, 3.69, 3.905,
    3.977, 3.961, 3.94, 3.994, 3.95, 3.860, 3.96, 3.592, 3.681, 3.861,
    3.66, 3.995, 4.01, 3.999, 3.99, 4.004, 3.700, 4.008, 3.62, 3.970,
    3.64, 3.847, 3.62, 3.646, 3.674, 3.601, 4.02, 3.603, 3.61, 4.009,
    4.01, 3.615, 3.672, 3.898, 3.95, 3.607, 3.70, 3.978, 3.65, 4.027,
    3.645, 3.643, 3.89, 3.635, 3.86, 3.631, 3.92, 3.635, 3.511, 3.539,
    3.83, 3.925, 3.97, 3.646, 3.66, 3.931, 4.028, 3.665, 3.68, 3.984,
    3.66, 3.893, 3.60, 3.699, 3.997, 3.936, 3.97, 3.627, 3.53, 3.695,
    3.98, 3.587, 3.680, 3.888, 3.92, 3.953, 3.84, 3.645, 4.04, 3.692,
    3.910, 3.672, 3.95, 3.961, 3.95, 3.904, 3.92, 3.984, 3.721, 3.927,
    3.62, 4.038, 4.04, 3.627, 3.77, 3.983, 3.658, 4.034, 3.77
]

# use the new class boundaries to calculate the frequency distribution
class_boundaries = np.arange(3.5, 4.1, 0.06)
class_boundaries = np.append(class_boundaries, 4.1)  # 确保包含最后一个上限
plt.figure(figsize=(10, 6))
# set the font size to 18 and the font family to Times New Roman
plt.hist(data, bins=class_boundaries, color='skyblue', edgecolor='black')
plt.xlabel('Weight (g)')  # X axis label
plt.xticks(class_boundaries)  # set the X axis scale
plt.ylabel('Num')  # Y axis label
# add the grid line
plt.grid(axis='y', alpha=0.75)
# display the plot
plt.show()