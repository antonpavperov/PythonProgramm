import math

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

def find_optimal_angle(d1_yards, d2_feet, h_yards, v_sand_mph, n):
    d1_feet = d1_yards * 3
    h_feet = h_yards * 3
    v_sand_fps = v_sand_mph * 5280 / 3600

    best_time = float('inf')
    best_angle = 0

    for theta1 in range(0, 901):
        theta1_deg = theta1 / 10.0
        try:
            time = calculate_rescue_time(
                d1_yards=d1_yards,
                d2_feet=d2_feet,
                h_yards=h_yards,
                v_sand_mph=v_sand_mph,
                n=n,
                theta1_degrees=theta1_deg
            )
            if time < best_time:
                best_time = time
                best_angle = theta1_deg
        except (ValueError, OverflowError):
            continue

    return best_angle, best_time


def display_result(time_seconds, theta1_degrees, is_optimal=False):
    if is_optimal:
        print(f"Оптимальный угол движения: {theta1_degrees:.1f}°")
        print(f"Минимальное время спасения: {round(time_seconds, 1)} секунды")
    else:
        print(f"Если спасатель начнёт движение под углом {theta1_degrees}°, "
              f"он достигнет утопающего через {round(time_seconds, 1)} секунды.")


def main():
    user_data = get_user_input()
    if user_data is None:
        return

    optimal_angle, min_time = find_optimal_angle(
        d1_yards=user_data['d1'],
        d2_feet=user_data['d2'],
        h_yards=user_data['h'],
        v_sand_mph=user_data['v_sand'],
        n=user_data['n']
    )

    display_result(min_time, optimal_angle, is_optimal=True)

if __name__ == "__main__":
    main()
