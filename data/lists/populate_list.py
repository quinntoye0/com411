def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("\nChoose a direction from the options below:")
    movement = directions()
    for x in range(len(movement)):
        print(f"{x}: {movement[x]}")
    option = int(input("Enter a direction: "))
    return movement[option]


def run():
    route = []
    print("\nWorking out potential escape route...")
    for x in range(5):
        route.append(menu())
    print(f"\nEscape route: {route}")

run()