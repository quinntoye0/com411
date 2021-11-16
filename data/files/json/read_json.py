import json

def read(file):
    with open(file) as file:
        data = json.load(file)
        city = data["city"]
        bots = data["bots"]
        population = data["population"]

        print(f"City Name: {city}")
        print(f"Population Size: {population}")
        for x in range(bots):
            bot_name = bots["name"]

            print(f"Bot Name: {bot_name}")



def run():
    read("robocity.json")


if __name__ == "__main__":
    run()
