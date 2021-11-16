import csv


def export(file_path, vals):
    print("\nExporting...")

    with open(file_path, "a") as file:

        for x in range(vals):
            bot_id = input("\nInput bot ID(num): ")
            bot_name = input("Input bot name: ")
            bot_paint = input("Input bot paint: ")
            write_data = f"\n{bot_id},{bot_name},{bot_paint}"
            file.write(write_data)


def run():
    export("exported_bots.csv", 2)


if __name__ == "__main__":
    run()
