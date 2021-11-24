import json


def read(file):
    with open(file) as file:
        data = json.load(file)
        city = data["city"]
        bots = data["bots"]
        population = data["population"]

        print(f"\nCity Name: {city}")
        print(f"\nPopulation Size: {population}")
        for bot in bots:
            bot_name = bot["name"]
            bots_stats = bot["stats"]
            bots_stats_speed = bots_stats["speed"]
            bots_stats_strength = bots_stats["strength"]
            print(f"\nBot Name: {bot_name}\nSpeed: {bots_stats_speed}\nStrength: {bots_stats_strength}")


def run():
    read("robocity.json")


if __name__ == "__main__":
    run()
