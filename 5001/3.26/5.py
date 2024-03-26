import numpy as np
import matplotlib.pyplot as plt

# 设置字体新罗马大小18
plt.rcParams['font.size'] = 18
plt.rcParams['font.family'] = 'Times New Roman'
# 已知概率
probabilities = np.array([0.0625, 0.25, 0.375, 0.25, 0.0625])
tails_outcomes = np.arange(5)  # 0到4次尾面的次数

# 计算累积分布
cumulative_probabilities = np.cumsum(probabilities)

# 绘制概率分布图
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.bar(tails_outcomes, probabilities, color='skyblue')
plt.title('Probability Distribution')
plt.xlabel('Num')
plt.xlim(-0.5, 4.5)
plt.ylabel('Probability')
plt.xticks(tails_outcomes)

# 绘制累积概率分布图，调整为在每个坐标轴的数字处加上概率值
plt.subplot(1, 2, 2)
plt.step(tails_outcomes, cumulative_probabilities, where='post', color='darkorange', linewidth=2)
plt.title('Cumulative Probability Distribution')
plt.xlabel('Num')
plt.ylabel('Cumulative Probability')
plt.ylim(0, 1)
plt.xlim(-0, 4)
plt.xticks(tails_outcomes)
plt.grid(axis='y')

plt.tight_layout()
plt.show()
