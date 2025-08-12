from parser import getInput
from turing import machine


def main():

    user_data = getInput()

    file_path = user_data["file_path"]
    input_str = user_data["input_str"]

    machine(file_path, input_str)


if __name__ == "__main__":
    main()
