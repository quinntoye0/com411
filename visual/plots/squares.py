"""# marker styles can be specified using single characters
# these include o for circles, s for squares, ^ for triangle up, v for triangle down

plt.plot(x, y, 'o')   # will display circle markers
plt.plot(x, y, 's')   # will display square markers

# similarly, we can control the line styles
# these include - for solid lines, -- for dashed lines, -. for dash-dot lines, : for dotted lines

plt.plot(x, y, 'o-')  # will display circle markers with a solid line
plt.plot(x, y, 'o--') # will display circle markers with a dashed line
plt.plot(x, y, 'o:')  # will display circle markers with a dotted line

# colors can be specified using single characters where r is red, b is blue, g is green, etc.
# supported colours include red, blue, green, cyan, magenta, yellow, black and white.

plt.plot(x, y, 'yo')   # will display yellow markers
plt.plot(x, y, 'ro--') # will display a red dashed line"""


import matplotlib.pyplot as plt


def small():
    x = [3, 3, 4, 4, 3]
    y = [3, 4, 4, 3, 3]

    plt.plot(x, y, 'ro:')



def medium():
    x = [2, 2, 5, 5, 2]
    y = [2, 5, 5, 2, 2]

    plt.plot(x, y, 'gs--')


def large():
    x = [1, 1, 6, 6, 1]
    y = [1, 6, 12, 1, 1]

    plt.plot(x, y, "b^-")


def run():
    small()
    medium()
    large()

    plt.show()


if __name__ == "__main__":
    run()

