import menu.menu as menu
import my_io.checked_input as ci
from tasks import task1
from tasks import task2
from tasks import task3
from tasks import task4
from tasks import task5
import inspect


def main():
    run = True
    while run:
        action = menu.show_menu()
        match action:
            case 1:
                try:
                    x = ci.input_float()
                    precision = ci.input_float()
                    res = task1.calculate_series_iterations(x, precision)
                except ArithmeticError:
                    print("Calculation took too long and was aborted")
                except ValueError:
                    print(f"Argument {x} not in function domain")
                else:
                    print("Number of iterations to reach precision " +
                          f"{precision}: {res}")

            case 2:
                res = task2.multiplicator()
                print(f"Result: {res}")

                pass
            case 3:
                res = task3.analyze_text(input("Enter text to be analyzed:"))
                print("Number of numeric characters and uppercase letters: " +
                      f"{res}")
                pass
            case 4:
                number_of_words, longest_index, longest = task4.analyze_text()
                print(f"Number of words in given text: {number_of_words}.\n" +
                      f"The longest word is {longest} " +
                      f"on position {longest_index + 1}")
                pass
            case 5:
                min_abs_index, min_abs, sum = task5.calculate_floats()
                print(f"Number with lowest absolute value: {min_abs} " +
                      f"with index {min_abs_index}.\n" +
                      f"Sum after first positive: {sum}")

                pass
            case 6:
                func_num = ci.input_int()
                match func_num:
                    case 1:
                        help(task1.calculate_series_iterations)
                    case 2:
                        help(task2.multiplicator)
                    case 3:
                        help(task3.analyze_text)
                    case 4:
                        help(task4.analyze_text)
                    case 5:
                        help(task5.calculate_floats)
                    case _:
                        print("Unknown function")
                pass
            case 7:
                run = False
                print("Exiting...")
                break


if __name__ == "__main__":
    main()
