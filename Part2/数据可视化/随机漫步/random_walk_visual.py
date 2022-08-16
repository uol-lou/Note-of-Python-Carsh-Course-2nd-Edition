import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:

    rw = RandomWalk()

    rw.fill_walk()
    rw.get_point_value()

    plt.style.use("classic")

    fig, ax = plt.subplots()

    ax.scatter(rw.x_value, rw.y_value, s=5)

    keep_running = input("Would you like another one? y/n")

    plt.show()

    if keep_running == "n":
        break
