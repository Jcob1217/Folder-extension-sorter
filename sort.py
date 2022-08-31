import pathlib
import shutil
import os

current_dir = os.getcwd()

for file in os.listdir(current_dir):
    try:
        if file != "sort.py" and os.path.isfile(file):
            name, extension = os.path.splitext(file)
            if extension != "":
                destination = os.path.join(current_dir, extension)
            else:
                destination = os.path.join(current_dir, ".other")
            if not os.path.exists(destination):
                os.mkdir(destination)
            shutil.move(os.path.join(current_dir, file), destination)
    except Exception as e:
        shutil.move(os.path.join(current_dir, file), os.path.join(destination, file))
