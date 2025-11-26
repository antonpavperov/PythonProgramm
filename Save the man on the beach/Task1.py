import math

d1 = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) =>:"))
print(d1)
d1_feet = d1 * 3

d2 = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) =>:"))
print(d2)

h = float(input("Введите боковое смещение между спасателем и утопающим, h (ярды) =>:"))
print(h)
h_feet = h * 3

v_sand = float(input("Введите скорость движения спасателя по песку, v_sand (мили в час) =>:"))
print(v_sand)
v_sand_fps = v_sand * 5280/3600

n = float(input("Введите коэффициент замедления спасателя при движении в воде, n =>"))
print(n)

theta1 = float(input("Введите направление движения спасателя по песку, theta1 (градусы)"))
print(theta1)
theta1_radians = math.radians(theta1)


x = d1_feet * math.tan(theta1_radians)

L1 = math.sqrt(x ** 2 + d1_feet ** 2)
print(L1)
L2 = math.sqrt((h_feet - x) ** 2 + d2 ** 2)
print(L2)
v_swim = v_sand_fps / n

t = 1 / v_sand_fps * (L1 + n * L2)
print(float(input(f"Если спасатель начнёт движение под углом theta1, равным 39 градусам, он достигнет утопащего через {round(t, 1)}  секунды")))


