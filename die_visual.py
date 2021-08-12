import pygal

from die import Die

# Created die D6.
die = Die()
# Simulation of a series of throws with saving the results in the list.
num_roll = 1000
results = [die.roll() for roll_num in range(num_roll)]
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

hist = pygal.Bar()
hist.title = f"Results of rolling one D{die.num_sides} {num_roll} times."
hist.x_labels = [str(i) for i in range(1, die.num_sides)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add(f'D{die.num_sides}', frequencies)
hist.render_to_file('die_visual.svg')
