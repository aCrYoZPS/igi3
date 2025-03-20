def show_menu():
    pass


def menu_item(menu_number: int):
    def decorator(func):
        def wrapper(*args):
            print(f"Starting task number {menu_number}")
            func(*args)

        return wrapper

    return decorator
