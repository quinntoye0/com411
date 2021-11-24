import csv


def read(file):
    with open(file) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"\nHeadings\n{headings}")

        print("\nValues:")
        for values in csv_reader:
            print(values)


def run():
    read("bots.csv")


if __name__ == "__main__":
    run()
