import numpy as np
import matplotlib.pyplot as plt

# set the font size to 18 and the font family to Times New Roman
plt.rcParams['font.size'] = 18
plt.rcParams['font.family'] = 'Times New Roman'
# known probabilities
probabilities = np.array([0.0625, 0.25, 0.375, 0.25, 0.0625])
tails_outcomes = np.arange(5)  # 0到4次尾面的次数
# calculate the cumulative distribution
cumulative_probabilities = np.cumsum(probabilities)
# plot the probability distribution
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.bar(tails_outcomes, probabilities, color='skyblue')
plt.title('Probability Distribution')
plt.xlabel('Num')
plt.xlim(-0.5, 4.5)
plt.ylabel('Probability')
plt.xticks(tails_outcomes)
# plot the cumulative probability distribution, adjust to add the probability value at each coordinate axis
plt.subplot(1, 2, 2)
plt.step(tails_outcomes, cumulative_probabilities, where='post', color='darkorange', linewidth=2)
plt.title('Cumulative Probability Distribution')
plt.xlabel('Num')
plt.ylabel('Cumulative Probability')
plt.ylim(0, 1)
plt.xlim(-0, 4)
plt.xticks(tails_outcomes)
plt.grid(axis='y')
# adjust the layout
plt.tight_layout()
# display the plot
plt.show()