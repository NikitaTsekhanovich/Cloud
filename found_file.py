import os
import tracemalloc


def found_file(file_name, folder):
    tracemalloc.start()
    try:
        for element in os.scandir(folder):
            if element.name == file_name:
                return element.name
    except FileNotFoundError:
        print("Not found folder")