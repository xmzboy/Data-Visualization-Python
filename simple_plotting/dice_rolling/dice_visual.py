from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice

dice = Dice()
dice_2 = Dice()

results = []
roll_count = 50000

for roll_num in range(roll_count):
    results.append(dice.roll() + dice_2.roll())

frequencies = []
max_result = dice.num_sides + dice_2.num_sides
for value in range(2, max_result + 1):
    frequencies.append(results.count(value))

x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title=f'Results of rolling two D{dice.num_sides} {roll_count} times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename=f'two_d{dice.num_sides}_{roll_count}_rolls.html')