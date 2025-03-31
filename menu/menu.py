from my_io.checked_input import input_int
from functools import wraps


def show_menu() -> int:
    while True:
        menu_intro = "Lab Work #3. Choose a task (1-5)," + \
            " 6 <task_number> for help, 7 for quit"
        print(menu_intro)

        n = input_int()
        if n > 7 or n < 1:
            print("Invalid option")
            continue

        return n


def menu_item(menu_number: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Starting task number {menu_number}")
            return func(*args, **kwargs)

        return wrapper

    return decorator
