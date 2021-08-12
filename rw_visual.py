import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Building a random walk and plotting points on a diagram.
    rw = RandomWalk(100000)
    rw.fill_walk()
    plt.figure(dpi=128, figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=1)
    # Select the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=100)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
