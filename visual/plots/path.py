import matplotlib.pyplot as plt


def coordinate():
    x = input("\nInput x value: ")
    y = input("\nInput y value: ")

    return x, y


def path():
    x_values = []
    y_values = []

    print("\nRetrieving path...")

    for x in range(4):
        vals = coordinate()
        x_values.append(vals[0])
        y_values.append(vals[1])

    return x_values, y_values


def run():
    values = path()

    plt.xlabel("poopy x values")
    plt.ylabel("stinky y values")
    plt.plot(values[0], values[1], 'yo-.')
    plt.show()


if __name__ == "__main__":
    run()




