import pygal

from die import Die

# Created dice D6.
die_1 = Die()
die_2 = Die(10)

# Simulation of a series of throws with saving the results in the list.
num_roll = 50000
results = [die_1.roll() + die_2.roll() for _ in range(num_roll)]
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

hist = pygal.Bar()
hist.title = f"Results of rolling two D{die_1.num_sides} + D{die_2.num_sides} {num_roll} times."
hist.x_labels = [str(i) for i in range(1, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add(f'D{die_1.num_sides} + D{die_2.num_sides}', frequencies)
hist.render_to_file('dice_6_10_visual.svg')
