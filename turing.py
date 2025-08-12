import json

def machine(file_path, input_str):

    with open(file_path, "r", encoding="utf-8") as f:
        file_content = json.load(f)

    transitions = file_content.get("transitions", [])
    final_states = set(file_content.get("final_states", []))

    blank = "_"
    tape = [blank] * 10 + list(input_str) + [blank] * 10
    head = 10
    current_state = "q0"
    step = 0

    while True:

        step += 1
        current_char = tape[head] if head < len(tape) else blank
        current_tape = "".join(tape).strip(blank)
        current_head = " " * head + "^"

        print(f"step {step}\nstate {current_state}\ntape {current_tape}\n{current_head}")

        if current_state in final_states:
            print("ACCEPT...")
            return True

        current_transition = None
        for t in transitions:
            if t["current_state"] == current_state and t["read"] == current_char:
                current_transition = t
                break

        if current_transition is None:
            current_state = "q_reject"

            print(f"{current_state}\n REJECT...")
            return False

        tape[head] = current_transition["write"]
        current_state = current_transition["next_state"]

        move = current_transition["move"].upper()
        if move == "R":
            head += 1
            if head >= len(tape):
                tape.append(blank)
        elif move == "L":
            if head > 0:
                head -= 1
            else:
                tape.insert(0, blank)
        else:
            pass
