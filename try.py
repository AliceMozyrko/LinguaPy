from mypackage import *

def is_valid_number(value):
    try:
        return float(value)
    except ValueError:
        return None

def get_float_input(prompt):
    while True:
        value = input(prompt)
        number = is_valid_number(value)
        if number is not None:
            return number
        else:
            print("Помилка: введіть допустиме число.")

def main():
    figures = {
        "1": "коло",
        "2": "прямокутник",
        "3": "квадрат",
        "4": "прямокутний трикутник"
    }
    
    while True:
        print("\nВиберіть фігуру:")
        for key, value in figures.items():
            print(f"{key}. {value}")
        figure_choice = input("\nВаш вибір (введіть просто число відповідне до фігури): ").strip()

        if figure_choice == "1":  
            print("\nДоступні операції для кола:")
            print("1. Обчислити площу кола")
            print("2. Обчислити довжину кола")
            print("3. Обчислити площу сектора кола")
            print("4. Обчислити довжину дуги кола")
            print("5. Перевірити, чи знаходиться точка всередині або на межі кола.")
            operation = input("\nВаш вибір: ").strip()
            radius = get_float_input("\nВведіть радіус кола: ")

            if operation == "1": 
                print(f"Площа кола: {circle_area(radius)}")
            elif operation == "2":
                print(f"Довжина кола: {circle_length(radius)}")
            elif operation == "3":
                central_angle = get_float_input("Введіть центральний кут сектора: ")
                print(f"Площа сектора кола: {sector_area(central_angle, radius)}")
            elif operation == "4":
                central_angle = get_float_input("Введіть центральний кут дуги: ")
                print(f"Довжина дуги кола: {arc_length(central_angle, radius)}")
            elif operation == "5":
                x = get_float_input("Введіть координату x точки: ")
                y = get_float_input("Введіть координату y точки: ")
                print(f"Чи знаходиться точка всередині кола: {is_point_inside(radius, x, y)}")
            else:
                print("Помилка: недоступна операція.")

        elif figure_choice == "2":  
            print("\nДоступні операції для прямокутника:")
            print("1. Обчислити площу прямокутника")
            print("2. Обчислити периметр прямокутника")
            print("3. Обчислити діагональ прямокутника")
            print("4. Перевірити, чи є фігура прямокутником")
            operation = input("\nВаш вибір: ")
            length = get_float_input("\nВведіть довжину прямокутника: ")
            width = get_float_input("Введіть ширину прямокутника: ")

            if operation == "1":
                print(f"Площа прямокутника: {rectangle_area(length, width)}")
            elif operation == "2":
                print(f"Периметр прямокутника: {rectangle_perimeter(length, width)}")
            elif operation == "3":
                print(f"Діагональ прямокутника: {rectangle_diagonal(length, width)}")
            elif operation == "4":
                angle1 = get_float_input("\nВведіть перший кут: ")
                angle2 = get_float_input("Введіть другий кут: ")
                angle3 = get_float_input("Введіть третій кут: ")
                angle4 = get_float_input("Введіть четвертий кут: ")
                print(f"Чи є фігура прямокутником: {is_rectangle(angle1, angle2, angle3, angle4)}")
            else:
                print("Помилка: недоступна операція.")

        elif figure_choice == "3":  
            print("\nДоступні операції для квадрата:")
            print("1. Обчислити площу квадрата")
            print("2. Обчислити периметр квадрата")
            print("3. Обчислити діагональ квадрата")
            print("4. Обчислити радіус вписаного кола")
            print("5. Обчислити радіус описаного кола")
            operation = input("\nВаш вибір: ")
            side_length = get_float_input("\nВведіть довжину сторони квадрата: ")

            if operation == "1":
                print(f"Площа квадрата: {square_area(side_length)}")
            elif operation == "2":
                print(f"Периметр квадрата: {square_perimeter(side_length)}")
            elif operation == "3":
                print(f"Діагональ квадрата: {square_diagonal(side_length)}")
            elif operation == "4":
                print(f"Радіус вписаного кола: {square_inradius(side_length)}")
            elif operation == "5":
                print(f"Радіус описаного кола: {square_circumradius(side_length)}")
            else:
                print("Помилка: недоступна операція.")

        elif figure_choice == "4":  
            print("\nДоступні операції для прямокутного трикутника:")
            print("1. Обчислити площу прямокутного трикутника")
            print("2. Обчислити гіпотенузу прямокутного трикутника")
            print("3. Обчислити висоту, проведену до гіпотенузи")
            print("4. Обчислити радіус вписаного кола")
            print("5. Обчислити радіус описаного кола")
            operation = input("\nВаш вибір: ")
            leg1 = get_float_input("\nВведіть перший катет: ")
            leg2 = get_float_input("Введіть другий катет: ")

            if operation == "1":
                print(f"Площа прямокутного трикутника: {triangle_area(leg1, leg2)}")
            elif operation == "2":
                print(f"Гіпотенуза трикутника: {find_hypotenuse(leg1, leg2)}")
            elif operation == "3":
                print(f"Висота, проведена до гіпотенузи: {altitude_to_hypotenuse(leg1, leg2)}")
            elif operation == "4":
                print(f"Радіус вписаного кола: {triangle_inradius(leg1, leg2)}")
            elif operation == "5":
                print(f"Радіус описаного кола: {triangle_circumradius()}")
            else:
                print("Помилка: недоступна операція.")

        else:
            print("Помилка: недоступна фігура.")
        
        repeat = input("\nБажаєте виконати іншу операцію? (так/ні): ").strip().lower()
        if repeat != "так":
            print("Дякуємо за користування!")
            break

if __name__ == "__main__":
    main()
