from checked_input import input_int


def show_menu() -> int:
    while True:
        menu_intro = "Lab Work #3. Choose a task (1-5), 6 for quit, 7 <task_number> for help"
        print(menu_intro)

        n = input_int()
        if n > 7 or n < 1:
            print("Invalid option")
            continue

        return n


def menu_item(menu_number: int):
    def decorator(func):
        def wrapper(*args):
            print(f"Starting task number {menu_number}")
            return func(*args)

        return wrapper

    return decorator
