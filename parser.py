from pathlib import Path as pt


def getInput():

    languages = {
        "1": "palindrome.json",
        "2": "anbn.json",
        "3": "equal_a_b.json",
        "4": "wcw.json",
    }

    print("\nSelect The Desired Language For The Test:")
    print("------------------------------------------------")

    print("1. palindrome")
    print("2. a^n b^n")
    print("3. n(a) = n(b)")
    print("4. w c w")

    print("------------------------------------------------\n")

    while True:
        choice = input("Enter Your Choice: ").strip()
        if choice in languages:
            break
        print("ERROR: Invalid input; Please Enter a Number Between 1 and 4\n")

    input_str = input("Enter Your Language: ").strip().lower()

    file_path = pt(__file__).resolve().parent / "transitions" / languages[choice]

    return {"file_path": str(file_path), "input_str": input_str}
