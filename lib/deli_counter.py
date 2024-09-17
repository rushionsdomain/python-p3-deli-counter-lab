def line(deli):
    """Displays the current line at the deli."""
    if not deli:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently: "
        line_status += ", ".join(f"{i+1}. {name}" for i, name in enumerate(deli))
        print(line_status)

def take_a_number(deli, name):
    """Adds a person to the end of the line and prints a welcome message."""
    position = len(deli) + 1
    deli.append(name)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(deli):
    """Serves the first person in line and removes them from the queue."""
    if not deli:
        print("There is nobody waiting to be served!")
    else:
        person = deli.pop(0)
        print(f"Currently serving {person}.")