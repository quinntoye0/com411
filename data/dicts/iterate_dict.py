def pattern():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


def display_keys(data):
    print("\nKeys:")
    for key in data:
        print(key)


def display_values(data):
    print("\nValues:")
    for value in data.values():
        print(value)

def display_pairs(data):
    print("\nPairs:")
    for key, value in data:
        print(f"{key}: {value}")


def run():
    data = pattern()
    print(f"Dictionaaary:\n{data}")

    display_keys(data)
    display_values(data)
    display_pairs(data)


if __name__ == "__main__":
    run()