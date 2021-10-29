def steps():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods


def run():
    return_list = steps()
    good_steps = []
    bad_steps = []
    val = 1
    for x in range(len(return_list)):
        if return_list[val] >= 50:
            bad_steps.append(return_list[x])
        else:
            good_steps.append(return_list[x])
        val += 2
    print(f"\nGood steps: {len(good_steps)}\nBad steps: {len(bad_steps)}")


if __name__ == "__main__":
    run()