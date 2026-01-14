import math


def show_menu():
    print("\n--- Інженерний калькулятор ---")
    print("Доступні операції: +, -, *, /, ^, sqrt, sin, cos")
    print("Введіть 'exit', щоб вийти.")


def calculate():
    while True:
        show_menu()
        choice = input("Оберіть операцію: ").strip().lower()

        if choice == "exit":
            print("Програма завершена.")
            break

        if choice in ("+", "-", "*", "/", "^"):
            try:
                a = float(input("Введіть перше число: "))
                b = float(input("Введіть друге число: "))

                if choice == "+":
                    print(f"Результат: {a + b}")
                elif choice == "-":
                    print(f"Результат: {a - b}")
                elif choice == "*":
                    print(f"Результат: {a * b}")
                elif choice == "/":
                    print(f"Результат: {a / b}")
                elif choice == "^":
                    print(f"Результат: {math.pow(a, b)}")
            except ValueError:
                print("Помилка: введіть коректне число!")
            except ZeroDivisionError:
                print("Помилка: ділення на нуль!")

        elif choice in ("sqrt", "sin", "cos"):
            try:
                num = float(input("Введіть число: "))
                if choice == "sqrt":
                    print(f"Результат: {math.sqrt(num)}")
                elif choice == "sin":
                    print(f"Результат: {math.sin(math.radians(num))} "
                          f"(для {num}°)")
                elif choice == "cos":
                    print(f"Результат: {math.cos(math.radians(num))} "
                          f"(для {num}°)")
            except ValueError:
                print("Помилка: введіть коректне число!")
        else:
            print("Невідома операція, спробуйте ще раз.")


calculate()

