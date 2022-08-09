import matplotlib.pyplot as plt
from random import choice

input_values = [i for i in range(-5000, 5000)]
squares = [i**3 for i in range(-5000, 5000)]

styles = ['Solarize_Light2', 'bmh', 'ggplot', 'seaborn', 'seaborn-notebook', 'seaborn-whitegrid']
plt.style.use(choice(styles))

fig, ax = plt.subplots()

ax.scatter(input_values, squares, c=squares, cmap=plt.cm.RdBu, s=20)
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of value', fontsize=14)
ax.tick_params(axis='both', labelsize=14)

plt.show()
