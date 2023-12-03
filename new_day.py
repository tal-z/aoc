import os
import shutil
import argparse


def copy_directory(source_dir, destination_dir):
    try:
        shutil.copytree(source_dir, destination_dir)
        print(f"Directory '{source_dir}' copied to '{destination_dir}' successfully.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="Copy the contents of a directory to another with a specified name.")
    parser.add_argument("destination_name", help="Name of the destination directory")

    args = parser.parse_args()

    source_dir = "daily_template"
    destination_name = args.destination_name
    destination_dir = os.path.join(os.getcwd(), destination_name)

    if os.path.exists(destination_dir):
        print(f"Error: Destination directory '{destination_dir}' already exists.")
    else:
        copy_directory(source_dir, destination_dir)


if __name__ == "__main__":
    main()
