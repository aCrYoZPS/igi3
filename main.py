import my_io.menu as menu
import my_io.checked_input as ci
from tasks import task1
from tasks import task2
from tasks import task3
from tasks import task4
from tasks import task5


def main():
    run = True
    while run:
        action = menu.show_menu()
        match action:
            case 1:
                try:
                    x = ci.input_float()
                    res = task1.calculate_series(x)
                except ArithmeticError:
                    print("Calculation took too long and was aborted")
                except ValueError:
                    print(f"Argument {x} not in function domain")
                else:
                    print(f"Value of series sum: {res}")

            case 2:
                res = task2.multiplicator()

                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass


if __name__ == "__main__":
    main()
