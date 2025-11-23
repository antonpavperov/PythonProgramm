import math

def validate_input(value, min_val=None, max_val=None):
    try:
        num = float(value)
        if min_val is not None and num < min_val:
            return False
        if max_val is not None and num > max_val:
            return False
        return True
    except (ValueError, TypeError):
        return False


def get_user_input():
    inputs = {}

    try:
        inputs['d1'] = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) =>:"))
        inputs['d2'] = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) =>:"))
        inputs['h'] = float(input("Введите боковое смещение между спасателем и утопающим, h (ярды) =>:"))
        inputs['v_sand'] = float(input("Введите скорость движения спасателя по песку, v_sand (мили в час) =>:"))
        inputs['n'] = float(input("Введите коэффициент замедления спасателя при движении в воде, n =>"))
        inputs['theta1'] = float(input("Введите направление движения спасателя по песку, theta1 (градусы)"))
    except ValueError:
        print("Ошибка: введите числа!")
        return None

    if not validate_input(inputs['d1'], min_val=0.1):
        print("d1 должно быть положительным числом!")
        return None
    if not validate_input(inputs['d2'], min_val=0.1):
        print("d2 должно быть положительным числом!")
        return None
    if not validate_input(inputs['h'], min_val=0.1):
        print("h должно быть положительным числом!")
        return None
    if not validate_input(inputs['v_sand'], min_val=0.1):
        print("v_sand должно быть положительным числом!")
        return None
    if not validate_input(inputs['n'], min_val=1.0):
        print("n должно быть не меньше 1!")
        return None
    if not validate_input(inputs['theta1'], min_val=0, max_val=90):
        print("theta1 должно быть от 0 до 90 градусов!")
        return None

    return inputs


def calculate_rescue_time(d1_yards, d2_feet, h_yards, v_sand_mph, n, theta1_degrees):
    d1_feet = d1_yards * 3
    h_feet = h_yards * 3
    v_sand_fps = v_sand_mph * 5280 / 3600  # мили/ч → футы/сек
    v_swim_fps = v_sand_fps / n

    theta1_radians = math.radians(theta1_degrees)
    x = d1_feet * math.tan(theta1_radians)
    L1 = math.sqrt(x ** 2 + d1_feet ** 2)
    L2 = math.sqrt((h_feet - x) ** 2 + d2_feet ** 2)

    t = (L1 + n * L2) / v_sand_fps
    return t


def display_result(time_seconds, theta1_degrees):
    print(f"Если спасатель начнёт движение под углом {theta1_degrees}°, "
          f"он достигнет утопающего через {round(time_seconds, 1)} секунды.")


def main():
    user_data = get_user_input()
    if user_data is None:
        return

    result = calculate_rescue_time(
        d1_yards=user_data['d1'],
        d2_feet=user_data['d2'],
        h_yards=user_data['h'],
        v_sand_mph=user_data['v_sand'],
        n=user_data['n'],
        theta1_degrees=user_data['theta1']
    )

    display_result(result, user_data['theta1'])

if __name__ == "__main__":
    main()
