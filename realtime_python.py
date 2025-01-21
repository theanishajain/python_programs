import os
folders = input("Please enter the folders with space ").split()
for folder in folders:
    files = os.listdir(folder)
    print(files)