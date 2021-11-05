def observed():
    observations = []

    for x in range(5):
        user_observe = input("\nPlease enter an observation: ")
        observations.append(user_observe)

    return observations


def remove_observations(observations):
    choice = "Y"
    while choice == "Y":
        choice = input("\nDo you wish to remove an observation (Y/N)? ").upper()
        if choice == "Y":
            remove_obs = input("\nWhat observation do you wish to remove? ")
            observations.remove(remove_obs)
            print("DONE!")
    return observations






def run():
    print("\nCounting observations...")
    observed_items = observed()
    observed_items = remove_observations(observed_items)
    observed_times = set()

    print("\nObservations:")
    for x in range(len(observed_items)):
        data = observed_items.count(observed_items[x])
        observed_times.add((observed_items[x], data))

        print(f"{observed_times[x]}")


if __name__ == "__main__":
    run()