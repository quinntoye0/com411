import matplotlib.pyplot as plt
import random


def data():
    paths = {}

    line_style = input("\nEnter line style (:, --, -): ")
    line_colour = input("\nEnter line colour (r, g, b, y): ").lower()
    marker_style = input("\nEnter marker style (o, s, p, ^): ")

    paths["linestyle"] = line_style
    paths["color"] = line_colour
    paths["marker"] = marker_style

    return paths


def generate():
    lines = int(input("\nEnter number of lines to display: "))
    for i in range(lines):
        values = data()

        x = random.randint(0, 20)
        y = random.randint(0, 20)

        plt.plot(x, y, **values)
        plt.show()


def run():
    print("\nRunning...")
    generate()
    print("\nCOMPLETE")


if __name__ == "__main__":
    run()
