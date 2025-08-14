from parser import getInput
from turing import machine
from utils import clear


def main():

    while True:
        user_data = getInput()

        if user_data["input_str"].lower() == "q":
            print("\nGoodbye! Exiting The Program... \U0001f44b\n")
            break

        file_path = user_data["file_path"]
        input_str = user_data["input_str"]

        machine(file_path, input_str)

        input("\n" + "-" * 33 + "\n\u2728 Press Enter To Continue...\u2728 ")
        clear()


if __name__ == "__main__":
    main()
