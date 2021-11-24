import json


def read(file):
    print("\nReading...")
    with open(file) as file:
        json_data = json.load(file)
    print("Done!")
    return json_data


def save(file_path, json_data):
    print("\nExporting...")
    with open(file_path, "w") as file:
        json.dump(json_data, file, indent=4)
    print("DONE!")


def run():
    json_data = read("robocity.json")
    save("exported.json", json_data)


if __name__ == "__main__":
    run()
