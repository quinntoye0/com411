import csv


def extract(file):
    print("\nExtracting...")

    with open(file) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)

        names = ""
        for values in csv_reader:
            names = names + values[1] + "\n"

        print(f"\nDONE! The extracted names are follows: \n{names}")


def run():
    extract("bots.csv")


if __name__ == "__main__":
    run()
