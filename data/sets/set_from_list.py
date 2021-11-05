def observed():
    observations = []

    for x in range(7):
        user_observe = input("\nPlease enter an observation: ")
        observations.append(user_observe)

    return observations


def run():
    print("\nCounting observations...")
    observed_items = observed()

    observed_times = set()

    for x in range(len(observed_items)):
        data = observed_items.count(observed_items[x])
        temp_tuple = (observed_items[x], data)
        observed_times.add(temp_tuple)

    print(observed_times)


if __name__ == "__main__":
    run()

