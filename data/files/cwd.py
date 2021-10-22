import os
path = os.getcwd()

print(f"\nProcessing...")
print(f"The current working directory is: {path}")
print("The current directory contains the following files: ")

for file in os.listdir(path):
    print(file)
